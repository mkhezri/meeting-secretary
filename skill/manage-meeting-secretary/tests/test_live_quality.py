import sys
import unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from check_gates import live_answer_mode,persist_qa_ready,scoped_rule_ready,metric_rate,dispatch_ready

class V11Gates(unittest.TestCase):
    def test_private_fact(self): self.assertEqual(live_answer_mode(True,True,True,True),'answer_with_source')
    def test_shared_screen_unknown(self): self.assertEqual(live_answer_mode(True,True,False,True),'withhold_restricted_content')
    def test_participant_not_allowed(self): self.assertEqual(live_answer_mode(True,True,True,False),'withhold_restricted_content')
    def test_unsupported(self): self.assertEqual(live_answer_mode(False,True,True,True),'unverified')
    def test_stale_price(self): self.assertEqual(live_answer_mode(True,False,True,True),'dated_context_only_recheck')
    def test_conflicting_sources(self): self.assertEqual(live_answer_mode(True,True,True,True,True),'present_conflict')
    def test_live_proposal_no_send_authority(self):
        a={'action_id':'A','revision':1,'review_status':'proposed'}
        self.assertFalse(dispatch_ready(a,{},'send','participant','x'))
    def qa_auth(self): return {'status':'approved','authorization_ref':'synthetic:owner','meeting_id':'M','destination':'private-store','audience':'owner','operation':'persist_qa'}
    def test_qa_persistence_explicit(self): self.assertTrue(persist_qa_ready(self.qa_auth(),'M','private-store','owner'))
    def test_no_qa_persistence(self): self.assertFalse(persist_qa_ready({},'M','private-store','owner'))
    def test_no_log_to_participants(self): self.assertFalse(persist_qa_ready(self.qa_auth(),'M','private-store','participants'))
    def rule(self): return {'status':'approved','authorization_ref':'synthetic:approval','correction_source':'synthetic:correction','scope':'company-A/project-X','version':2,'positive_regression_passed':True,'unrelated_scope_regression_passed':True}
    def test_scoped_rule(self): self.assertTrue(scoped_rule_ready(self.rule(),'company-A/project-X'))
    def test_no_global_generalization(self): self.assertFalse(scoped_rule_ready(self.rule(),'global'))
    def test_proposal_rule_not_applied(self):
        r=self.rule();r['status']='proposed';self.assertFalse(scoped_rule_ready(r,r['scope']))
    def test_counterexample_required(self):
        r=self.rule();r['unrelated_scope_regression_passed']=False;self.assertFalse(scoped_rule_ready(r,r['scope']))
    def test_no_metrics_without_review(self): self.assertEqual(metric_rate(0,100,False),{'status':'not_measured','rate':None})
    def test_zero_denominator(self): self.assertEqual(metric_rate(0,0,True),{'status':'N/A','rate':None})
    def test_observed_rate(self): self.assertEqual(metric_rate(2,10,True)['rate'],0.2)
    def test_invalid_metric(self):
        with self.assertRaises(ValueError): metric_rate(11,10,True)

if __name__ == '__main__': unittest.main()
