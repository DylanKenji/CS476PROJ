# Description: This file contains the routes for the web application.
from app import app, db
from flask import render_template, request, redirect, url_for, session, flash, current_app
from app.models import Students, Employers, Jobs
from werkzeug.utils import secure_filename
import os

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
# routes to home page
@app.route('/')
def index():
    return render_template("home.html")


@app.route('/login')
def login():
    return render_template('login.html')


# routes user to the student registration page
@app.route('/createStudent', methods=['POST', 'GET'])
def createStudent():
    form = request.form
    if request.method == 'POST':
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
    else:
        return render_template('createStudent.html')



# routes to login page after registering new employer
@app.route('/createEmployer', methods=['POST'])
def emp_login():
    if request.method == 'POST':
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
    else:
        return render_template('createEmployer.html')


# validates student logging in
@app.route('/std_profile_login', methods=['POST', 'GET'])
def std_profile_login():
    if request.method == 'POST':
        form = request.form
        student = Students.query.filter_by(email=form['email']).first()
        if student is not None:
            if student.check_password(form['password']):
                session["student"] = student.id
                return redirect(url_for('profileStudent'))
            else:
                print("password check failed")
                return render_template('login.html')
        else:
            print("no user found")
            return render_template('login.html')
    else:
        return render_template('login.html')


# if student is logged in, they can view their profile
@app.route('/profileStudent', methods=['POST', 'GET'])
def profileStudent():
    if "student" in session:
        student = session["student"]
        student = Students.query.filter_by(id=student).first()
        return render_template('profileStudent.html', students=student)
    return render_template('profileStudent.html')


@app.route('/editStudent', methods=['GET', 'POST'])
def editStudent():
    UPLOAD_FOLDER = app.config['UPLOAD_FOLDER']
    if "student_key" in session:
        student_id = session["student_key"]
        student = Students.query.get(student_id)

        if request.method == 'POST':
            # Update student information based on form data
            student.first_name = request.form['studentfirstName']
            student.last_name = request.form['studentlastName']
            student.email = request.form['studentEmail']
            student.major = request.form['studentMajor']
            student.looking_for_job = bool(request.form.get('studentAvailability'))

            # Update password if new password is provided and matches confirmation
            new_password = request.form.get('newPassword')
            confirm_password = request.form.get('confirmPassword')
            if new_password and confirm_password and new_password == confirm_password:
                student.set_password(new_password)

            # Update avatar if a new file is uploaded
            if 'newstudentAvatar' in request.files:
                avatar_file = request.files['newstudentAvatar']
                if avatar_file.filename != '':
                    # Securely save the avatar file on the server
                    if allowed_file(avatar_file.filename):
                        filename = secure_filename(avatar_file.filename)
                        avatar_file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                        # Update the student's avatar attribute with the file path (or URL)
                        student.avatar = os.path.join(app.config['UPLOAD_FOLDER'], filename)

            try:
                db.session.commit()
                return redirect(url_for('editStudent'))
            except Exception as e:
                # Handle any exceptions that may occur during the database commit
                print(e)

        # If it's a GET request or after processing a POST request, render the template
        return render_template('profileStudent.html', student=student)

    # If 'student_key' is not in the session or the student doesn't exist, redirect to login
    return redirect(url_for('login'))  # Assuming you have a 'login' route


# Function to check if the uploaded file has an allowed extension
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/jobListings')
def jobListings():
    # Query the database for the 20 most recent jobs
    jobListings = Jobs.query.order_by(Jobs.date_created.desc()).limit(20).all()
    return render_template('jobListings.html', jobs=jobListings)


@app.route('/postJob', methods=['GET', 'POST'])
def postJob():
    if "employer_key" in session:
        employer_id = session["employer_key"]
        if request.method == 'POST':
            form = request.form
            job = Jobs(
                title=form['Title'],
                description=form['Description'],
                location=form['adress'],
                deadline=form['deadline'],
                employer_id=employer_id
            )
            db.session.add(job)
            db.session.commit()
            return redirect(url_for('jobListings'))
        else:
            return render_template('postJob.html')
    else:
        return redirect(url_for('login'))
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
                student.first_name = request.form['first_name']
            student.last_name = request.form['last_name']
            student.email = request.form['email']
            student.major = request.form['major']
            student.bio = request.form['bio']
            student.avatar = request.form['avatar']
            student.major = request.form['major']
            student.looking_for_job = request.form['looking_for_job']
            student.resume = request.form['resume']\
"""
