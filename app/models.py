from app import db


class Students(db.Model):
    __tablename__ = 'STUDENTS'
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, unique=True, nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)
    resume = db.Column(db.Text)
    major = db.Column(db.Text)
    looking_for_job = db.Column(db.Boolean)
    bio = db.Column(db.Text)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_updated = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())


class Employers(db.Model):
    __tablename__ = 'EMPLOYERS'
    id = db.Column(db.Integer, primary_key=True)
    company_name = db.Column(db.String(200), nullable=False)
    user_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    is_hiring = db.Column(db.Boolean)
    address = db.Column(db.String(200), nullable=False)
    phone = db.Column(db.String(15))
    password = db.Column(db.String(50), nullable=False)
    bio = db.Column(db.Text)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_updated = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())



class Jobs(db.Model):
    __tablename__ = 'JOBS'
    id = db.Column(db.Integer, primary_key=True)
    job_title = db.Column(db.String(200), nullable=False)
    job_description = db.Column(db.Text, nullable=False)
    job_location = db.Column(db.String(200), nullable=False)
    city = db.Column(db.String(200), nullable=False)
    major_required = db.Column(db.Text)
    filled = db.Column(db.Boolean)
    hours = db.Column(db.Text)
    work_term = db.Column(db.Integer)
    pay = db.Column(db.Integer)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_updated = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    deadline = db.Column(db.DateTime)
