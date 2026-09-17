import re
import secrets
from flask import Blueprint, request, jsonify
from backend.models import EmployeeModel, UserPreparationModel, CompanyPrepModel

auth_bp = Blueprint("auth", __name__)

EMAIL_REGEX = r"^[\w\.-]+@[\w\.-]+\.\w+$"


@auth_bp.route("/api/auth/register", methods=["POST"])
def register():
    """
    Candidate Registration Endpoint:
    - Validates all required candidate details.
    - Ensures email is strictly unique in database.
    - If email already exists, returns 'Email already registered. Please login.'
    - Hashes password securely before database insertion.
    - Initializes user preparation profile.
    """
    try:
        data = request.get_json() or {}
        
        name = data.get("name", "").strip()
        email = data.get("email", "").strip().lower()
        password = data.get("password", "")
        confirm_password = data.get("confirm_password", "")
        qualification = data.get("qualification", "").strip()
        skills = data.get("skills", "").strip()
        experience = data.get("experience", "").strip()
        job_role = (data.get("job_role", "") or data.get("jobRole", "")).strip()
        target_company = (data.get("target_company") or "Tata Consultancy Services (TCS)").strip()
        target_role = (data.get("target_role") or job_role or "Software Engineer").strip()

        # Validation: All core fields required
        if not all([name, email, password, qualification, skills, experience, job_role]):
            return jsonify({
                "success": False,
                "message": "All fields are required. Please fill in all information."
            }), 400

        # Valid email format
        if not re.match(EMAIL_REGEX, email):
            return jsonify({
                "success": False,
                "message": "Please enter a valid email address."
            }), 400

        # Password minimum 6 characters
        if len(password) < 6:
            return jsonify({
                "success": False,
                "message": "Password must be at least 6 characters long."
            }), 400

        # Confirm password matching
        if confirm_password and password != confirm_password:
            return jsonify({
                "success": False,
                "message": "Passwords do not match."
            }), 400

        # Check unique email: exact prompt message
        existing_employee = EmployeeModel.get_by_email(email)
        if existing_employee:
            return jsonify({
                "success": False,
                "message": "Email already registered. Please login."
            }), 409

        # Create employee in DB (password is securely hashed inside EmployeeModel.create)
        new_employee_id = EmployeeModel.create(
            name=name,
            email=email,
            password=password,
            qualification=qualification,
            skills=skills,
            experience=experience,
            job_role=job_role,
            target_company=target_company,
            target_role=target_role
        )

        new_employee = EmployeeModel.get_by_id(new_employee_id)

        return jsonify({
            "success": True,
            "message": "Account created successfully! Please login.",
            "employee": new_employee
        }), 201

    except Exception as e:
        return jsonify({
            "success": False,
            "message": f"Registration failed due to a server error: {str(e)}"
        }), 500


@auth_bp.route("/api/auth/login", methods=["POST"])
def login():
    """
    Candidate Login Endpoint:
    - Verifies credentials against database.
    - Zero user creation/insertion during login.
    - Rejects unknown emails with 'No account found with this email. Please register first.'
    - Rejects incorrect passwords with 'Incorrect email or password.'
    - Generates session token and returns full candidate details.
    """
    try:
        data = request.get_json() or {}
        email = data.get("email", "").strip().lower()
        password = data.get("password", "")

        if not email or not password:
            return jsonify({
                "success": False,
                "message": "Email and password are required."
            }), 400

        # Look up existing user by trimmed lowercased email
        employee = EmployeeModel.get_by_email(email)
        if not employee:
            return jsonify({
                "success": False,
                "message": "No account found with this email. Please register first."
            }), 404

        # Verify password securely against stored hash
        if not EmployeeModel.verify_password(employee["password"], password):
            return jsonify({
                "success": False,
                "message": "Incorrect email or password."
            }), 401

        # Generate authenticated session token
        session_token = f"emp_token_{secrets.token_hex(20)}"

        # Ensure user preparation record is active
        target_company = employee.get("target_company") or "Tata Consultancy Services (TCS)"
        target_role = employee.get("target_role") or employee.get("job_role") or "Software Engineer"
        comp = CompanyPrepModel.get_by_name_or_slug(target_company)
        comp_slug = comp["slug"] if comp else "tcs"
        UserPreparationModel.get_or_create(employee["id"], comp_slug, target_company, target_role)

        # Build clean employee response object (excluding password hash)
        clean_employee = {
            "id": employee["id"],
            "name": employee["name"],
            "email": employee["email"],
            "qualification": employee.get("qualification", ""),
            "skills": employee.get("skills", ""),
            "experience": employee.get("experience", ""),
            "job_role": employee.get("job_role", ""),
            "target_company": target_company,
            "target_company_slug": comp_slug,
            "target_role": target_role,
            "is_admin": bool(employee.get("is_admin", 0)),
            "token": session_token
        }

        return jsonify({
            "success": True,
            "message": "Login successful!",
            "token": session_token,
            "employee": clean_employee
        }), 200

    except Exception as e:
        return jsonify({
            "success": False,
            "message": f"Login failed due to a server error: {str(e)}"
        }), 500


@auth_bp.route("/api/auth/validate-session", methods=["GET"])
def validate_session():
    """
    Validates candidate session and returns latest profile.
    """
    try:
        employee_id = request.args.get("employee_id", type=int)
        if not employee_id:
            return jsonify({"success": False, "message": "employee_id required."}), 400

        employee = EmployeeModel.get_by_id(employee_id)
        if not employee:
            return jsonify({"success": False, "message": "Session expired or invalid user."}), 401

        target_company = employee.get("target_company") or "Tata Consultancy Services (TCS)"
        target_role = employee.get("target_role") or employee.get("job_role") or "Software Engineer"
        comp = CompanyPrepModel.get_by_name_or_slug(target_company)
        comp_slug = comp["slug"] if comp else "tcs"

        clean_employee = {
            "id": employee["id"],
            "name": employee["name"],
            "email": employee["email"],
            "qualification": employee.get("qualification", ""),
            "skills": employee.get("skills", ""),
            "experience": employee.get("experience", ""),
            "job_role": employee.get("job_role", ""),
            "target_company": target_company,
            "target_company_slug": comp_slug,
            "target_role": target_role,
            "is_admin": bool(employee.get("is_admin", 0))
        }

        return jsonify({
            "success": True,
            "valid": True,
            "employee": clean_employee
        }), 200

    except Exception as e:
        return jsonify({"success": False, "message": f"Error validating session: {str(e)}"}), 500


@auth_bp.route("/api/employee/profile", methods=["GET"])
def get_profile():
    """
    Fetches full candidate profile by ID or email.
    """
    try:
        employee_id = request.args.get("id", type=int)
        email = request.args.get("email", type=str)

        if employee_id:
            employee = EmployeeModel.get_by_id(employee_id)
        elif email:
            employee = EmployeeModel.get_by_email(email)
            if employee:
                employee.pop("password", None)
        else:
            return jsonify({
                "success": False,
                "message": "Please provide an employee id or email."
            }), 400

        if not employee:
            return jsonify({
                "success": False,
                "message": "Employee not found."
            }), 404

        # Attach active target company slug
        target_company = employee.get("target_company") or "Tata Consultancy Services (TCS)"
        comp = CompanyPrepModel.get_by_name_or_slug(target_company)
        employee["target_company_slug"] = comp["slug"] if comp else "tcs"

        return jsonify({
            "success": True,
            "data": employee
        }), 200

    except Exception as e:
        return jsonify({
            "success": False,
            "message": f"Error fetching profile: {str(e)}"
        }), 500


@auth_bp.route("/api/employee/goal", methods=["POST"])
def set_career_goal():
    """
    Updates employee's target company and target job role.
    """
    try:
        data = request.get_json() or {}
        employee_id = data.get("employee_id")
        target_company = (data.get("target_company") or "Tata Consultancy Services (TCS)").strip()
        target_role = (data.get("target_role") or "Software Engineer").strip()

        if not employee_id:
            return jsonify({"success": False, "message": "employee_id is required."}), 400

        updated = EmployeeModel.set_career_goal(int(employee_id), target_company, target_role)
        if updated:
            comp = CompanyPrepModel.get_by_name_or_slug(target_company)
            comp_slug = comp["slug"] if comp else "tcs"
            return jsonify({
                "success": True,
                "message": f"Career goal updated to {target_company} — {target_role}!",
                "target_company": target_company,
                "target_company_slug": comp_slug,
                "target_role": target_role
            }), 200
        else:
            return jsonify({"success": False, "message": "Failed to update career goal."}), 400

    except Exception as e:
        return jsonify({"success": False, "message": f"Error updating goal: {str(e)}"}), 500
