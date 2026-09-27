# -*- coding: utf-8 -*-
"""
Test Security & Anti-Cheating Routes (Flask Blueprint).

Provides real-time proctoring and audit endpoints for assessment sessions:
- POST /api/test/<attempt_id>/violation : Records tab-switches, window blurs, fullscreen exits,
  increments server-authoritative count, and returns auto_submit status.
- GET /api/test/<attempt_id>/security-report : Returns full proctoring audit trail,
  violation count, and clean/flagged attempt status for result cards and history.

Viva Core Logic:
1. Server Authority: The server maintains and increments the violation count.
   The frontend cannot tamper with or reset the counter on reload.
2. Max Threshold: Default limit is 3 violations. Upon 3rd violation, server returns
   auto_submit = True, forcing test submission.
3. Audit Log: Every security event is persisted in `test_security_logs` with a timestamp
   and duration away in seconds.
"""

import logging
from flask import Blueprint, request, jsonify
from backend.models import TestSecurityModel, EmployeeModel

logger = logging.getLogger("test_security")
test_security_bp = Blueprint("test_security", __name__)


def _extract_employee_id():
    """Extracts employee_id from header, query, or json body."""
    # Header
    h_id = request.headers.get("X-Employee-Id") or request.headers.get("employee-id")
    if h_id:
        try:
            return int(h_id)
        except ValueError:
            pass

    # JSON Body
    if request.is_json:
        data = request.get_json(silent=True) or {}
        b_id = data.get("employee_id")
        if b_id:
            try:
                return int(b_id)
            except ValueError:
                pass

    # Query param
    q_id = request.args.get("employee_id")
    if q_id:
        try:
            return int(q_id)
        except ValueError:
            pass

    return 0


@test_security_bp.route("/api/test/<attempt_id>/violation", methods=["POST"])
def record_test_violation(attempt_id: str):
    """
    Records an anti-cheating violation during an active test:
    Body:
      - event_type: 'tab_switch' | 'window_blur' | 'fullscreen_exit' | 'copy_paste_attempt' | 'right_click'
      - duration_away_seconds: float (optional)
      - employee_id: int (optional, falls back to header/auth)
    Returns:
      {
        "success": true,
        "test_attempt_id": "...",
        "event_type": "...",
        "violation_count": 2,
        "max_allowed": 3,
        "auto_submit": false
      }
    """
    try:
        data = request.get_json(silent=True) or {}
        employee_id = data.get("employee_id") or _extract_employee_id()

        if not employee_id:
            return jsonify({
                "success": False,
                "message": "employee_id is required to record test security violation."
            }), 400

        event_type = data.get("event_type", "tab_switch")
        duration_away = data.get("duration_away_seconds")

        logger.warning(
            f"Security violation on test {attempt_id} by employee {employee_id}: "
            f"type={event_type}, duration={duration_away}s"
        )

        result = TestSecurityModel.record_violation(
            employee_id=int(employee_id),
            test_attempt_id=str(attempt_id),
            event_type=event_type,
            duration_away_seconds=duration_away
        )

        return jsonify(result), 200

    except Exception as e:
        logger.error(f"Error in record_test_violation: {e}", exc_info=True)
        return jsonify({"success": False, "message": str(e)}), 500


@test_security_bp.route("/api/test/<attempt_id>/security-report", methods=["GET"])
def get_test_security_report(attempt_id: str):
    """
    Returns the proctoring audit log and violation summary for a test attempt:
    - total_violations
    - max_allowed
    - is_clean (true if 0 violations)
    - auto_submitted (true if test was auto-submitted due to 3+ violations)
    - events (list of timestamped violation events)
    """
    try:
        employee_id = _extract_employee_id()
        report = TestSecurityModel.get_security_report(
            test_attempt_id=str(attempt_id),
            employee_id=employee_id if employee_id > 0 else None
        )
        return jsonify(report), 200

    except Exception as e:
        logger.error(f"Error in get_test_security_report: {e}", exc_info=True)
        return jsonify({"success": False, "message": str(e)}), 500
