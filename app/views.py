from app import app, db
from flask import render_template, request
from app.models import Students, Employers, Jobs

@app.route('/')
def index():
    return render_template("createStudent.html")

@app.route('/std_login', methods=['POST'])
def std_login():
    form = request.form
    createStudent = Students(
        student_id=form['student_id'],
        first_name=form['first_name'],
        last_name=form['last_name'],
        email=form['email'],
        password=form['password'],
    )
    db.session.add(createStudent)
    db.session.commit()
    return render_template("login.html")

@app.route('/emp_login', methods=['POST'])
def emp_login():
    form = request.form
    createEmployer = Employers(
        user_name=form['user_name'],
        company_name=form['company_name'],
        company_address=form['address'],
        company_phone=form['phone'],
        email=form['email'],
        password=form['password'],
    )
    db.session.add(createEmployer)
    db.session.commit()
    return render_template("login.html")

@app.route('/createEmployer')
def createEmployer():
    return render_template('createEmployer.html')


@app.route('/createStudent')
def createStudent():
    return render_template('createStudent.html')


@app.route('/editEmployer')
def editEmployer():
    return render_template('editEmployer.html')


@app.route('/editStudent')
def editStudent():
    return render_template('editStudent.html')


@app.route('/jobListings')
def jobListings():
    return render_template('jobListings.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/postJob')
def postJob():
    return render_template('postJob.html')


@app.route('/profileEmployer')
def profileEmployer():
    return render_template('profileEmployer.html')


@app.route('/profileStudent')
def profileStudent():
    return render_template('profileStudent.html')




"""

@app.route('/profileEmployer', methods=['POST'])
def ():
    student_db.emp_register(request.form)
    return "Success!"
"""