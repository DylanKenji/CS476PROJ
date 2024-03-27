# Description: This file contains the routes for the web application.
from app import app, db
from flask import render_template, request, redirect, url_for, session, flash, current_app
from sqlalchemy import func
from app.models import Students, Employers, Jobs, Applications
from werkzeug.utils import secure_filename
import os
import glob
from datetime import datetime
from flask import jsonify

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}


# routes to home page
@app.route('/')
def index():
    return render_template("home.html")


@app.route('/login', methods=['POST', 'GET'])
def login():
    return render_template('login.html')


@app.route('/creatingEmployer')
def gotoEmployer():
    return render_template('createEmployer.html')


@app.route('/creatingStudent')
def gotoStudent():
    return render_template('createStudent.html')


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
@app.route('/createEmployer', methods=['POST', 'GET'])
def emp_login():
    if request.method == 'POST':
        form = request.form
        createEmployer = Employers(
            first_name=form['first_name'],
            last_name=form['last_name'],
            company_name=form['company_name'],
            address=form['address'],
            phone=form['phone'],
            email=form['email'],
        )
        createEmployer.set_password(form['password'])
        db.session.add(createEmployer)
        db.session.commit()
        return render_template("login.html")
    else:
        return render_template('createEmployer.html')


# validates logging in
@app.route('/std_profile_login', methods=['POST', 'GET'])
def std_profile_login():
    if request.method == 'POST':
        form = request.form
        student = Students.query.filter(func.lower(Students.email) == func.lower(form['email'])).first()
        if student is not None:
            if student.check_password(form['password']):
                session["student"] = student.id
                return redirect(url_for('profileStudent'))
            else:
                flash("password check failed")
                return render_template('login.html')
        else:
            form = request.form
            if student in session:
                del session['student']
            employer = Employers.query.filter(func.lower(Employers.email) == func.lower(form['email'])).first()
            if employer is not None:
                if employer.check_password(form['password']):
                    session["employer"] = employer.id
                    return redirect(url_for('profileEmployer'))
                else:
                    flash("password check failed")
                    return render_template('login.html')
            else:
                print("no user found")
                return render_template('login.html')
    else:
        return render_template('createStudent.html')


# if student is logged in, they can view their profile
@app.route('/profileStudent', methods=['POST', 'GET'])
def profileStudent():
    if "student" in session:
        student = session["student"]
        student = Students.query.filter_by(id=student).first()
        return render_template('profileStudent.html', student=student)
    else:
        return redirect(url_for('login'))


@app.route('/profileEmployer', methods=['POST', 'GET'])
def profileEmployer():
    if "employer" in session:
        employer = session["employer"]
        employer = Employers.query.filter_by(id=employer).first()
        return render_template('profileEmployer.html', employer=employer)
    else:
        return redirect(url_for('login'))


@app.route('/editStudent', methods=['GET', 'POST'])
def editStudent():
    UPLOAD_FOLDER = app.config['UPLOAD_FOLDER']
    RESUME_FOLDER = app.config['RESUME_FOLDER']
    if "student" in session:
        student = session["student"]
        student = Students.query.get(student)

        if request.method == 'POST':
            # Update student information based on form data
            student.first_name = request.form['studentfirstName']
            student.last_name = request.form['studentlastName']
            student.email = request.form['studentEmail']
            student.major = request.form['studentMajor']
            student.looking_for_job = bool(request.form.get('studentAvailability'))
            # student.resume = request.form['newResume']

            # Update password if new password is provided and matches confirmation
            new_password = request.form.get('newPassword')
            if len(new_password) >= 5:
                confirm_password = request.form.get('confirmPassword')
                if new_password and confirm_password and new_password == confirm_password:
                    student.set_password(new_password)

            # Handle new resume file upload
            if 'newResume' in request.files:
                resume_file = request.files['newResume']
                if resume_file.filename != '':
                    if allowed_resume_file(resume_file.filename):
                        # Customize the new resume file name as needed
                        resume_filename = f"{student.first_name}_{student.last_name}_{student.id}_Resume.pdf"
                        # Save the uploaded resume with the new name
                        resume_file.save(os.path.join(RESUME_FOLDER, resume_filename))
                        # Update the student's resume attribute with the new filename
                        student.resume = resume_filename

            # Update avatar if a new file is uploaded
            if 'newstudentAvatar' in request.files:
                avatar_file = request.files['newstudentAvatar']
                if avatar_file.filename != '':
                    # Securely save the avatar file on the server
                    if allowed_file(avatar_file.filename):
                        # Generate the new avatar filename
                        avatar_filename = f"{student.first_name}_{student.last_name}_{student.id}_Avatar{os.path.splitext(avatar_file.filename)[1]}"

                        # Check if there's an existing avatar file with a different extension
                        old_avatar_path = os.path.join(app.config['UPLOAD_FOLDER'],
                                                       f"{student.first_name}_{student.last_name}_{student.id}_Avatar.*")
                        old_avatar_files = glob.glob(old_avatar_path)
                        for old_avatar_file in old_avatar_files:
                            os.remove(old_avatar_file)

                        # Save the uploaded avatar with the new name
                        avatar_file.save(os.path.join(app.config['UPLOAD_FOLDER'], avatar_filename))

                        # Update the student's avatar attribute with the new filename
                        student.avatar = avatar_filename

            try:
                db.session.commit()
                return redirect(url_for('editStudent'))
            except Exception as e:
                # Handle any exceptions that may occur during the database commit
                print(e)
        else:
            # If it's a GET request or after processing a POST request, render the template
            return render_template('editStudent.html', student=student)
    else:
        # If 'student_key' is not in the session or the student doesn't exist, redirect to login
        return redirect(url_for('login'))  # Assuming you have a 'login' route


# Function to check if the uploaded file has an allowed extension
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def allowed_resume_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'pdf', 'doc', 'docx'}


@app.route('/editEmployer', methods=['GET', 'POST'])
def editEmployer():
    UPLOAD_FOLDER = app.config['UPLOAD_FOLDER']
    if "employer" in session:
        employer = session["employer"]
        employer = Employers.query.get(employer)

        if request.method == 'POST':
            # Update employer information based on form data
            employer.first_name = request.form['employerfirstName']
            employer.last_name = request.form['employerlastName']
            employer.email = request.form['employerEmail']
            employer.company_name = request.form['employerCompany']
            employer.address = request.form['employerAddress']
            employer.phone = request.form['employerPhone']

            # Update password if new password is provided and matches confirmation
            new_password = request.form.get('newPassword')
            if len(new_password) >= 5:
                confirm_password = request.form.get('confirmPassword')
                if new_password and confirm_password and new_password == confirm_password:
                    employer.set_password(new_password)

            # Update avatar if a new file is uploaded
            if 'newemployerAvatar' in request.files:
                avatar_file = request.files['newemployerAvatar']
            if avatar_file.filename != '':
            # Securely save the avatar file on the server
                if allowed_file(avatar_file.filename):
                # Generate the new avatar filename
                    avatar_filename = f"{employer.first_name}_{employer.last_name}_{employer.id}_Avatar{os.path.splitext(avatar_file.filename)[1]}"

            # Save the uploaded avatar with the new name
                avatar_file.save(os.path.join(app.config['UPLOAD_FOLDER'], avatar_filename))

            # Update the employer's avatar attribute with the new filename
                employer.avatar = avatar_filename

            try:
                db.session.commit()
                return redirect(url_for('editEmployer'))
            except Exception as e:
                # Handle any exceptions that may occur during the database commit
                print(e)
        else:
            # If it's a GET request or after processing a POST request, render the template
            return render_template('editEmployer.html', employer=employer)


@app.route('/jobListings')
def jobListings():
    # Query the database for the 20 most recent jobs
    print(session)
    if "student" in session:
        student = session["student"]
        student = Students.query.filter_by(id=student).first()
        jobListings = Jobs.query.order_by(Jobs.date_created.desc()).limit(20).all()
        return render_template('jobListings.html', jobs=jobListings, student=student, employers="employers")
    elif "employer" in session:
        employer = session["employer"]
        employer_instance = Employers.query.filter_by(id=employer).first()
        if employer_instance:
            jobListings = Jobs.query.filter_by(company_name=employer_instance.company_name).order_by(Jobs.date_created.desc()).limit(20).all()
            return render_template('jobListings.html', jobs=jobListings, employer=employer_instance, student="student")
    else:
        return redirect(url_for('login'))


@app.route('/postJob', methods=['GET', 'POST'])
def postJob():
    if "employer" in session:
        employer = session["employer"]
        employer = Employers.query.get(employer)

        if request.method == 'POST':

            title = request.form['Title']
            description = request.form['Description']
            location = request.form['Address']
            deadline = request.form['Deadline']
            major_required = request.form['Major']
            pay = request.form['Pay']
            hours = request.form['Hours']

            deadline_datetime = datetime.strptime(deadline, '%Y-%m-%d')

            job = Jobs(
                job_title=title,
                job_description=description,
                job_location=location,
                deadline=deadline_datetime,
                major_required=major_required,
                pay=pay,
                hours=hours,
                avatar=employer.avatar,
                company_name=employer.company_name
            )

            db.session.add(job)
            db.session.commit()

            db.session.commit()

            return redirect(url_for('jobListings'))
        else:
            return render_template('postJob.html', employer=employer)
    else:
        return redirect(url_for('login'))


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))


def is_email_used(email):
    # Check if the email exists in the Employers table
    employer_exists = Employers.query.filter_by(email=email).first()
    # if the email exists in the Students table
    student_exists = Students.query.filter_by(email=email).first()
    # Return True if the email is used by either an employer or a student, False otherwise
    return employer_exists or student_exists


@app.route('/job/<int:job_id>')
def get_job_details(job_id):
    job = Jobs.query.get(job_id)
    if job:
        return {
            'avatar': job.avatar,
            'job_title': job.job_title,
            'company_name': job.company_name,
            'job_location': job.job_location,
            'date_created': job.date_created,
            'job_description': job.job_description,
            'major_required': job.major_required,
            'hours': job.hours,
            'pay': job.pay,

            # Add other job details as needed
        }
    else:
        return {'error': 'Job not found'}, 404


@app.route('/apply_for_job', methods=['POST'])
def apply_for_job():
    if 'student' not in session:
        # Redirect to login if student is not logged in
        return redirect(url_for('login'))

    # Get student ID from session
    student_id = session['student']

    # Get job ID from the request body
    data = request.json
    job_id = data.get('job_id')

    # Check if both student ID and job ID are provided
    if student_id and job_id:
        # Query the database to ensure the student and job exist
        student = Students.query.get(student_id)
        job = Jobs.query.get(job_id)

        if student and job:
            # Create a new application instance
            application = Applications(student_id=student_id, job_id=job_id)

            # Add the application to the database session and commit
            db.session.add(application)
            db.session.commit()

            # Respond with a success message
            return jsonify({'message': 'Application submitted successfully'}), 200
        else:
            # Handle case where student or job does not exist
            return jsonify({'error': 'Student or Job not found'}), 404
    else:
        # Handle case where student ID or job ID is missing
        return jsonify({'error': 'Student ID or Job ID is missing'}), 400