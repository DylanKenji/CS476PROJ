# The models are used to create the tables in the database.
from app import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.orm import relationship


# The Students class is used to create the STUDENTS table in the database.
class Students(db.Model):
    __tablename__ = 'STUDENTS'
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, unique=True, nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    resume = db.Column(db.Text)
    major = db.Column(db.Text, default=" ")
    looking_for_job = db.Column(db.Boolean)
    avatar = db.Column(db.String(200),default="Default.png")
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_updated = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    job_applications = relationship('Applications', backref='student', cascade='all, delete-orphan')


    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


# The Employers class is used to create the EMPLOYERS table in the database.
class Employers(db.Model):
    __tablename__ = 'EMPLOYERS'
    id = db.Column(db.Integer, primary_key=True)
    company_name = db.Column(db.String(200), nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    is_hiring = db.Column(db.Boolean)
    address = db.Column(db.String(200), nullable=False)
    phone = db.Column(db.String(15))
    password_hash = db.Column(db.String(128))
    avatar = db.Column(db.String(200), default="Default.png")
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_updated = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


# The Jobs class is used to create the JOBS table in the database.
class Jobs(db.Model):
    __tablename__ = 'JOBS'
    id = db.Column(db.Integer, primary_key=True)
    job_title = db.Column(db.String(200), nullable=False)
    job_description = db.Column(db.Text, nullable=False)
    job_location = db.Column(db.String(200), nullable=False)
    major_required = db.Column(db.Text)
    filled = db.Column(db.Boolean, default = False)
    hours = db.Column(db.Text)
    pay = db.Column(db.Float)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_updated = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    deadline = db.Column(db.DateTime)
    applicants = relationship('Applications', backref='job', cascade='all, delete-orphan')
    avatar = db.Column(db.String(200), default="Default.png")
    company_name = db.Column(db.String(200))


class Applications(db.Model):
    __tablename__ = 'Applications'
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('STUDENTS.id'))
    job_id = db.Column(db.Integer, db.ForeignKey('JOBS.id'))
