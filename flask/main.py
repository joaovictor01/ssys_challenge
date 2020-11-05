from flask import jsonify, request
from flask import json
from flask_migrate import Migrate

import datetime
import jwt

from app import app, db
from app.models import User, Employee, user_share_schema, users_share_schema, employee_share_schema, employees_share_schema
from app.authenticate import jwt_required

migrate = Migrate(app, db)


@app.shell_context_processor
def make_shell_context():
    return dict(
        app=app,
        db=db,
        User=User,
        Employee=Employee
    )


@app.route('/auth/register', methods=["POST"])
def register():
    username = request.json['username']
    email = request.json['email']
    password = request.json['password']

    user = User(
        username,
        email,
        password
    )

    db.session.add(user)
    db.session.commit()

    result = user_share_schema.dump(
        User.query.filter_by(email=email).first()
    )

    return jsonify(result)


@app.route('/auth/login', methods=["POST"])
def login():
    email = request.json['email']
    password = request.json['password']

    user = User.query.filter_by(email=email).first_or_404()

    if not user.verify_password(password):
        return jsonify({
            "error": "Invalid credentials!"
        }), 403

    payload = {
        "id": user.id,
        # token expires every 10 minutes
        "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=10)
    }

    token = jwt.encode(payload, app.config['SECRET_KEY'])

    return jsonify({"token": token.decode("utf-8")})


@app.route('/employees', methods=["GET"])
@jwt_required
def get_employee_list(current_user):
    result = employees_share_schema.dump(
        Employee.query.all()
    )

    return jsonify(result)


@app.route('/employees', methods=["POST"])
@jwt_required
def add_employee(current_user):
    name = request.json['name']
    email = request.json['email']
    department = request.json['department']
    salary = request.json['salary']
    birth_date = request.json['birth_date']

    employee = Employee(name, email, department, salary, birth_date)

    db.session.add(employee)
    db.session.commit()

    result = employee_share_schema.dump(
        Employee.query.filter_by(email=email).first()
    )

    return jsonify(result)


@app.route('/employees/<employee_id>', methods=["PUT"])
@jwt_required
def update_employee(current_user, employee_id):
    employee = Employee.query.filter_by(id=employee_id).first()

    if not employee:
        return jsonify({"message": "Employee not found."})

    employee.name = request.json['name']
    employee.email = request.json['email']
    employee.department = request.json['department']
    employee.salary = request.json['salary']
    employee.birth_date = request.json['birth_date']

    db.session.merge(employee)
    db.session.flush()
    db.session.commit()

    result = employee_share_schema.dump(
        Employee.query.filter_by(email=employee.email).first()
    )

    return jsonify(result)


@app.route('/employees/<employee_id>', methods=["DELETE"])
@jwt_required
def delete_employee(current_user, employee_id):
    employee = Employee.query.filter_by(id=employee_id).first()

    if not employee:
        return jsonify({"message": "Employee not found."})

    db.session.delete(employee)
    db.session.commit()

    return jsonify({"message": "The employee has been deleted."})


@app.route('/employees/<employee_id>', methods=["GET"])
@jwt_required
def get_employee_details(current_user, employee_id):
    employee = Employee.query.filter_by(id=employee_id).first()

    if not employee:
        return jsonify({"message": "Employee not found."})

    result = employee_share_schema.dump(
        Employee.query.filter_by(id=employee_id).first()
    )

    return jsonify(result)


@app.route('/reports/employees/age', methods=["GET"])
@jwt_required
def reports_by_age(current_user):
    query = Employee.query.order_by(Employee.birth_date)
    result = employees_share_schema.dump(
        Employee.query.order_by(Employee.birth_date.desc())
    )

    return jsonify(result)


@app.route('/reports/employees/salary', methods=["GET"])
@jwt_required
def reports_by_salary(current_user):
    query = Employee.query.order_by(Employee.salary)
    result = employees_share_schema.dump(
        Employee.query.order_by(Employee.salary)
    )
    return jsonify(result)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
