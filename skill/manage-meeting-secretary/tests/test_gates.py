import copy
import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from check_gates import dispatch_ready, closure_ready, operation_key, retry_decision

class Gates(unittest.TestCase):
    def setUp(self):
        self.a={'action_id':'A1','revision':1,'review_status':'approved','acceptance_criterion':'Checklist reviewed'}
        self.p={'status':'approved','actor':'synthetic-owner','authorization_ref':'synthetic:approval1','data_scope':'checklist','payload_digest':'h1','object_id':'A1','revision':1,'operation':'send','destination':'synthetic-recipient'}
    def test_missing_action_id(self):
        self.a.pop('action_id');self.p.pop('object_id')
        self.assertFalse(dispatch_ready(self.a,self.p,'send','synthetic-recipient','h1'))
    def test_missing_revision(self):
        self.a.pop('revision');self.p.pop('revision')
        self.assertFalse(dispatch_ready(self.a,self.p,'send','synthetic-recipient','h1'))
    def test_missing_closure_revision(self):
        a=self.completed();a.pop('revision');a['closure_acceptance'].pop('revision')
        self.assertFalse(closure_ready(a))
    def test_missing_operation_even_when_caller_matches(self):
        self.p.pop('operation')
        self.assertFalse(dispatch_ready(self.a,self.p,None,'synthetic-recipient','h1'))
    def test_missing_destination_even_when_caller_matches(self):
        self.p.pop('destination')
        self.assertFalse(dispatch_ready(self.a,self.p,'send',None,'h1'))
    def test_missing_evidence_identifiers(self):
        a=self.completed();a['evidence'][0].pop('id');a['closure_acceptance'].pop('evidence_id')
        self.assertFalse(closure_ready(a))
    def test_changed_evidence_version(self):
        a=self.completed();a['evidence'][0]['version']='v2'
        self.assertFalse(closure_ready(a))
    def test_unbound_evidence_version(self):
        a=self.completed();a['closure_acceptance'].pop('evidence_version')
        self.assertFalse(closure_ready(a))
    def test_changed_bound_evidence_digest(self):
        a=self.completed();a['closure_acceptance']['evidence_digest']='old';a['evidence'][0]['digest']='new'
        self.assertFalse(closure_ready(a))
    def test_exact_approval(self): self.assertTrue(dispatch_ready(self.a,self.p,'send','synthetic-recipient','h1'))
    def test_changed_revision(self):
        self.a['revision']=2
        self.assertFalse(dispatch_ready(self.a,self.p,'send','synthetic-recipient','h1'))
    def test_wrong_recipient(self): self.assertFalse(dispatch_ready(self.a,self.p,'send','other','h1'))
    def test_changed_payload(self): self.assertFalse(dispatch_ready(self.a,self.p,'send','synthetic-recipient','h2'))
    def test_other_operation(self): self.assertFalse(dispatch_ready(self.a,self.p,'invite','synthetic-recipient','h1'))
    def test_no_authority_source(self):
        self.p['authorization_ref']=None
        self.assertFalse(dispatch_ready(self.a,self.p,'send','synthetic-recipient','h1'))
    def test_proposal_not_approval(self):
        self.p['status']='proposed'
        self.assertFalse(dispatch_ready(self.a,self.p,'send','synthetic-recipient','h1'))
    def test_claim_not_closure(self):
        self.a['execution_status']='completion_claimed'
        self.assertFalse(closure_ready(self.a))
    def completed(self):
        a=copy.deepcopy(self.a)
        a['evidence']=[{'id':'E1','version':'v1','accessible':True,'relevant':True,'criterion_passed':True}]
        a['closure_acceptance']={'actor':'synthetic-owner','authorization_ref':'synthetic:accept','accepted_at':'2026-10-16T00:00:00Z','revision':1,'evidence_id':'E1','evidence_version':'v1'}
        return a
    def test_verified_closure(self): self.assertTrue(closure_ready(self.completed()))
    def test_inaccessible_evidence(self):
        a=self.completed();a['evidence'][0]['accessible']=False;self.assertFalse(closure_ready(a))
    def test_irrelevant_evidence(self):
        a=self.completed();a['evidence'][0]['relevant']=False;self.assertFalse(closure_ready(a))
    def test_stale_acceptance(self):
        a=self.completed();a['revision']=2;self.assertFalse(closure_ready(a))
    def test_key_stable_and_revision_specific(self):
        args=('M1','A1',1,'send','recipient')
        self.assertEqual(operation_key(*args),operation_key(*args))
        self.assertNotEqual(operation_key(*args),operation_key('M1','A1',2,'send','recipient'))
    def test_unknown_send_no_retry(self): self.assertEqual(retry_decision('uncertain',None),'hold_for_reconciliation')
    def test_accepted_send_no_retry(self): self.assertEqual(retry_decision('uncertain','accepted'),'record_acceptance_no_resend')
    def test_not_applied_recheck(self): self.assertEqual(retry_decision('uncertain','definitively_not_applied'),'recheck_authorization_before_retry')

if __name__ == '__main__': unittest.main()
