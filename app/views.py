# Description: This file contains the routes for the web application.
from app import app, db
from flask import render_template, request, redirect, url_for, session, flash
from app.models import Students, Employers, Jobs


# routes to home page
@app.route('/')
def index():
    return render_template("home.html")

@app.route('/login')
def login():
    return render_template('login.html')

# routes user to the student registration page
@app.route('/createStudent')
def createStudent():
    return render_template('createStudent.html')


# routes to login page after registering new student
@app.route('/std_registered', methods=['POST'])
def std_login():
    form = request.form
    createStudent = Students(
        student_id=form['student_id'],
        first_name=form['first_name'],
        last_name=form['last_name'],
        email=form['email'],

    )
    createStudent.set_password(form['password'])
    db.session.add(createStudent)
    db.session.commit()
    return render_template("login.html")


# routes to login page after registering new employer
@app.route('/emp_register', methods=['POST'])
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
    createEmployer.set_password(form['password'])
    db.session.add(createEmployer)
    db.session.commit()
    return render_template("login.html")


@app.route('/std_profile_login', methods=['POST'])
def std_profile_login():
    form = request.form
    student = Students.query.filter_by(email=form['email']).first()
    if student is not None :
        if student.check_password(form['password']):
            session["student"] = student.id
            return redirect(url_for('profileStudent'))
        else:
            print("password check failed")
            return render_template('login.html')
    else:
        print("no user found")
        return render_template('login.html')


@app.route('/profileStudent', methods=['POST', 'GET'])
def profileStudent():
    if "student" in session:
        student = session["student_key"]
        student = Students.query.filter_by(id=student).first()
        return render_template('profileStudent.html', students=student)
    return render_template('profileStudent.html')

@app.route('/editStudent')
def editStudent():
    form
    return render_template('editStudent.html')
"""
@app.route('/emp_profile_login', methods=['POST'])
def emp_profile_login():
    form = request.form
    employer = Employers.query.filter_by(email=form['email']).first()
    if employer is not None and employer.check_password(form['password']):
        return redirect(url_for('profileEmployer'))
    else:
        return render_template('login.html')


@app.route('/profileEmployer', methods=['POST', 'GET'])
def profileEmployer():
    return render_template('profileEmployer.html')


# routes to the creation page for the employer
@app.route('/createEmployer')
def createEmployer():
    return render_template('createEmployer.html')


@app.route('/editEmployer')
def editEmployer():
    return render_template('editEmployer.html')





@app.route('/jobListings')
def jobListings():
    return render_template('jobListings.html')


@app.route('/stdlogin')
def stdlogin():
    return render_template('login.html')


@app.route('/emplogin')
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