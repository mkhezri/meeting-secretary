"""Local synthetic gate checks; no connectors, persistence or live authority verification."""
import hashlib
import json

def operation_key(meeting, action, revision, operation, destination):
    payload = [meeting, action, revision, operation, destination]
    return hashlib.sha256(json.dumps(payload, ensure_ascii=False, separators=(',', ':')).encode()).hexdigest()

def dispatch_ready(action, approval, operation, destination, digest):
    if any(not isinstance(value, str) or not value.strip() for value in (operation, destination, digest)):
        return False
    if not action.get('action_id') or type(action.get('revision')) is not int or action['revision'] < 1:
        return False
    if not approval or approval.get('status') != 'approved':
        return False
    fields = ('actor', 'authorization_ref', 'data_scope', 'payload_digest')
    if any(not approval.get(k) for k in fields):
        return False
    return (action.get('review_status') == 'approved'
            and approval.get('object_id') == action.get('action_id')
            and approval.get('revision') == action.get('revision')
            and approval.get('operation') == operation
            and approval.get('destination') == destination
            and approval.get('payload_digest') == digest)

def closure_ready(action):
    if not action.get('action_id') or type(action.get('revision')) is not int or action['revision'] < 1:
        return False
    acceptance = action.get('closure_acceptance') or {}
    evidence = action.get('evidence') or []
    accepted_id = acceptance.get('evidence_id')
    accepted_version = acceptance.get('evidence_version')
    if any(not isinstance(value, str) or not value.strip() for value in (accepted_id, accepted_version)):
        return False
    return (bool(action.get('acceptance_criterion'))
            and acceptance.get('revision') == action.get('revision')
            and bool(acceptance.get('actor')) and bool(acceptance.get('authorization_ref'))
            and bool(acceptance.get('accepted_at'))
            and any(e.get('id') == accepted_id and e.get('accessible') is True
                    and e.get('relevant') is True and e.get('criterion_passed') is True
                    and e.get('version') == accepted_version
                    and (not acceptance.get('evidence_digest') or e.get('digest') == acceptance['evidence_digest'])
                    for e in evidence))

def retry_decision(outcome, provider_status):
    if outcome == 'uncertain':
        if provider_status == 'accepted': return 'record_acceptance_no_resend'
        if provider_status == 'definitively_not_applied': return 'recheck_authorization_before_retry'
        return 'hold_for_reconciliation'
    return 'inspect_tool_policy'

# Pure checks on supplied evidence. They do not verify identity, consent, freshness
# or approval authenticity; an authorized adapter/reviewer must establish those.
def live_answer_mode(source_verified, current_enough, audience_verified, audience_allowed, conflict=False):
    if not audience_verified or not audience_allowed:
        return 'withhold_restricted_content'
    if not source_verified:
        return 'unverified'
    if conflict:
        return 'present_conflict'
    if not current_enough:
        return 'dated_context_only_recheck'
    return 'answer_with_source'

def persist_qa_ready(authorization, meeting_id, destination, audience):
    return (bool(meeting_id) and bool(destination) and bool(audience)
            and authorization.get('status') == 'approved'
            and bool(authorization.get('authorization_ref'))
            and authorization.get('meeting_id') == meeting_id
            and authorization.get('destination') == destination
            and authorization.get('audience') == audience
            and authorization.get('operation') == 'persist_qa')

def scoped_rule_ready(rule, target_scope):
    return (bool(target_scope) and rule.get('status') == 'approved'
            and bool(rule.get('authorization_ref'))
            and bool(rule.get('correction_source'))
            and rule.get('scope') == target_scope
            and type(rule.get('version')) is int and rule['version'] > 0
            and rule.get('positive_regression_passed') is True
            and rule.get('unrelated_scope_regression_passed') is True)

def metric_rate(numerator, denominator, reviewed):
    if not reviewed:
        return {'status':'not_measured','rate':None}
    if type(numerator) is not int or type(denominator) is not int or numerator < 0 or denominator < 0 or numerator > denominator:
        raise ValueError('Invalid reviewed counts')
    return {'status':'N/A' if denominator == 0 else 'measured',
            'rate':None if denominator == 0 else numerator / denominator}


def template_scope_key(scope):
    """Exact organization-set match; unresolved keys never produce a key."""
    fields = ('company_id', 'business_domain', 'meeting_type')
    if not isinstance(scope, dict) or any(not isinstance(scope.get(k), str) or not scope[k].strip() or scope[k] == '*' for k in fields):
        return None
    orgs = scope.get('participant_organization_ids')
    if not isinstance(orgs, list) or not orgs or any(not isinstance(x, str) or not x.strip() or x == '*' for x in orgs):
        return None
    if len(orgs) != len(set(orgs)):
        return None
    return tuple(scope[k] for k in fields) + (tuple(sorted(orgs)),)


def visual_template_ready(variant, context):
    """Local evidence gate only. Does not approve minutes content or sharing."""
    key = template_scope_key(context)
    if key is None or key != template_scope_key(variant.get('scope')):
        return False
    approval = variant.get('visual_approval') or {}
    if (variant.get('status') != 'approved' or not variant.get('variant_id')
            or type(variant.get('revision')) is not int or variant['revision'] < 1
            or not variant.get('artifact_digest') or not variant.get('source_version')
            or not variant.get('text_structure_source')
            or approval.get('status') != 'approved'
            or approval.get('artifact_digest') != variant.get('artifact_digest')
            or approval.get('revision') != variant.get('revision')
            or any(not approval.get(k) for k in ('owner', 'authorization_ref', 'approved_at'))
            or (variant.get('visual_review') or {}).get('passed') is not True):
        return False
    branding_mode = variant.get('branding_mode', 'logos_required')
    if branding_mode == 'text_only':
        return bool(variant.get('branding_policy_ref')) and not variant.get('logos')
    if branding_mode != 'logos_required':
        return False
    logos = variant.get('logos') or []
    if not isinstance(logos, list) or any(not isinstance(l, dict) for l in logos):
        return False
    orgs = context['participant_organization_ids']
    # Every participant organization needs a sourced approved mark for official use.
    if len(logos) != len(orgs) or {l.get('organization_id') for l in logos} != set(orgs):
        return False
    return all(l.get('placeholder') is False and all(l.get(k) for k in
               ('asset_source', 'asset_version', 'approval_ref')) for l in logos)
