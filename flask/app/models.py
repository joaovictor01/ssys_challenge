from app import db, ma 
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

class User(db.Model):
    __tablename__="users"
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String(84),nullable=False)
    email = db.Column(db.String(84),nullable=False,unique=True)
    password = db.Column(db.String(128),nullable=False)

    def __init__(self,username,email,password):
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.password,password)
    
    def __repr__(self):
        return f"<User : {self.username} >"
    
class UserSchema(ma.Schema):
    class Meta:
        fields = ('id','username','email')

class Employee(db.Model):
    __tablename__="employees"
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(80),nullable=False)
    email = db.Column(db.String(80),nullable=False,unique=True)
    department = db.Column(db.String(50),nullable=False)
    # salary = db.Column(db.Numeric(precision=8, scale=2, decimal_return_scale=2),nullable=False)
    salary = db.Column(db.Float,nullable=False)
    birth_date = db.Column(db.String(10),nullable=False)


    def __init__(self,name,email,department,salary,birth_date):
        self.name = name
        self.email = email
        self.department = department
        self.salary = salary
        self.birth_date = datetime.strptime(birth_date,'%d-%m-%Y')
    
    def __repr__(self):
        return f"<User : {self.name} >"

class EmployeeSchema(ma.Schema):
    class Meta:
        fields = ('id','name','email','department','salary','birth_date')

user_share_schema = UserSchema()
users_share_schema = UserSchema(many=True)
employee_share_schema = EmployeeSchema()
employees_share_schema = EmployeeSchema(many=True)
        

