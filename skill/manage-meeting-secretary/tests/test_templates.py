import copy
import sys
import unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from check_gates import visual_template_ready, dispatch_ready

class ScopedTemplateTests(unittest.TestCase):
    def setUp(self):
        self.context = {'company_id':'SYN-ORG-A','business_domain':'internal_commerce','meeting_type':'minutes','participant_organization_ids':['SYN-ORG-A','Partner']}
        self.variant = {'variant_id':'synthetic-joint','revision':1,'scope':copy.deepcopy(self.context),'status':'approved','artifact_digest':'visual-sha','source_version':'1','text_structure_source':'synthetic:source','visual_approval':{'status':'approved','owner':'synthetic-owner','authorization_ref':'synthetic:visual-approval','approved_at':'2026-10-16','artifact_digest':'visual-sha','revision':1},'visual_review':{'passed':True},'logos':[{'organization_id':org,'placeholder':False,'asset_source':'synthetic:'+org,'asset_version':'1','approval_ref':'synthetic:logo-approval'} for org in self.context['participant_organization_ids']]}
    def test_explicit_text_only_branding(self):
        self.variant.update(branding_mode='text_only', branding_policy_ref='synthetic:policy', logos=[])
        self.assertTrue(visual_template_ready(self.variant,self.context))
    def test_text_only_needs_policy(self):
        self.variant.update(branding_mode='text_only', logos=[])
        self.assertFalse(visual_template_ready(self.variant,self.context))
    def test_unknown_branding_mode(self):
        self.variant['branding_mode']='unknown'
        self.assertFalse(visual_template_ready(self.variant,self.context))
    def test_text_only_still_needs_visual_approval(self):
        self.variant.update(branding_mode='text_only',branding_policy_ref='synthetic:policy',logos=[],visual_approval={})
        self.assertFalse(visual_template_ready(self.variant,self.context))
    def test_matching_approved_variant_reused(self): self.assertTrue(visual_template_ready(self.variant,self.context))
    def test_wrong_domain_reuse_blocked(self):
        self.context['business_domain']='foreign_commerce';self.assertFalse(visual_template_ready(self.variant,self.context))
    def test_other_company_blocked(self):
        self.context['company_id']='Another';self.assertFalse(visual_template_ready(self.variant,self.context))
    def test_other_meeting_type_blocked(self):
        self.context['meeting_type']='agenda';self.assertFalse(visual_template_ready(self.variant,self.context))
    def test_other_partner_blocked(self):
        self.context['participant_organization_ids']=['SYN-ORG-A','Other'];self.assertFalse(visual_template_ready(self.variant,self.context))
    def test_org_order_irrelevant(self):
        self.context['participant_organization_ids'].reverse();self.assertTrue(visual_template_ready(self.variant,self.context))
    def test_joint_logos_required(self):
        self.variant['logos'].pop();self.assertFalse(visual_template_ready(self.variant,self.context))
    def test_unknown_logo_placeholder_blocks_official_use(self):
        self.variant['logos'][1]['placeholder']=True;self.assertFalse(visual_template_ready(self.variant,self.context))
    def test_logo_source_required(self):
        del self.variant['logos'][1]['asset_source'];self.assertFalse(visual_template_ready(self.variant,self.context))
    def test_first_variant_needs_owner_approval(self):
        self.variant['visual_approval']={};self.assertFalse(visual_template_ready(self.variant,self.context))
    def test_approval_exact_visual_revision(self):
        self.variant['revision']=2;self.assertFalse(visual_template_ready(self.variant,self.context))
    def test_changed_artifact_needs_approval(self):
        self.variant['artifact_digest']='new';self.assertFalse(visual_template_ready(self.variant,self.context))
    def test_unresolved_organizations_block(self):
        self.context['participant_organization_ids']=None;self.assertFalse(visual_template_ready(self.variant,self.context))
    def test_no_autoapproval_future_content(self):
        self.assertTrue(visual_template_ready(self.variant,self.context))
        a={'action_id':'minutes-next','revision':1,'review_status':'proposed'}
        self.assertFalse(dispatch_ready(a,self.variant['visual_approval'],'send','partner','new-content-sha'))
    def test_visual_approval_no_sharing_authority(self):
        a={'action_id':'minutes-next','revision':1,'review_status':'approved'}
        self.assertFalse(dispatch_ready(a,self.variant['visual_approval'],'send','partner','new-content-sha'))

if __name__=='__main__': unittest.main()
