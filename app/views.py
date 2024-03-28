# Description: This file contains the routes for the web application.
from app import app, db
from flask import render_template, request, redirect, url_for, session, flash, current_app
from sqlalchemy import func, or_
from app.models import Students, Employers, Jobs, Applications
from werkzeug.utils import secure_filename
import os, glob
from datetime import datetime
from flask import jsonify

# Define the upload folder for avatar images
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}


# routes to home page
@app.route('/')
def index():
    return render_template("home.html")


# routes to the login page
@app.route('/login', methods=['POST', 'GET'])
def login():
    return render_template('login.html')


# routes to the creating employer page
@app.route('/creatingEmployer')
def gotoEmployer():
    return render_template('createEmployer.html')


# routes to the creating student page
@app.route('/creatingStudent')
def gotoStudent():
    return render_template('createStudent.html')


# routes user to the student registration page
@app.route('/createStudent', methods=['POST', 'GET'])
def createStudent():
    #save the form data
    form = request.form
    if request.method == 'POST':
        #check if email is already in use
        if is_email_used(form['email']):
            #if email is already in use, flash an error message and redirect to the createStudent page
            flash('Email already in use', 'error')
            return render_template('createStudent.html')

        #create a new student instance
        createStudent = Students(
            student_id=form['student_id'],
            first_name=form['first_name'],
            last_name=form['last_name'],
            email=form['email'],

        )
        #set the password for the student
        createStudent.set_password(form['password'])
        #add the student to the database
        db.session.add(createStudent)
        db.session.commit()
        #redirect to the login page
        return render_template("login.html")
    else:
        #if the request method is not POST, render the createStudent page
        return render_template('createStudent.html')


# routes to employer registration page
@app.route('/createEmployer', methods=['POST', 'GET'])
def emp_login():
    if request.method == 'POST':

        #save the form data
        form = request.form

        #check if email is already in use
        if is_email_used(form['email']):
            flash('Email already in use', 'error')
            return render_template('createEmployer.html')

        #create a new employer instance
        createEmployer = Employers(
            first_name=form['first_name'],
            last_name=form['last_name'],
            company_name=form['company_name'],
            address=form['address'],
            phone=form['phone'],
            email=form['email'],
        )
        #set the password for the employer
        createEmployer.set_password(form['password'])
        #add the employer to the database
        db.session.add(createEmployer)
        db.session.commit()
        #redirect to the login page
        return render_template("login.html")
    else:
        #if the request method is not POST, render the createEmployer page
        return render_template('createEmployer.html')


# Function to check if an email is already in use in the database
def is_email_used(email):
    # check if the email exists in the Employers table
    employer_exists = Employers.query.filter_by(email=email).first()
    # check if the email exists in the Students table
    student_exists = Students.query.filter_by(email=email).first()
    # return True if the email is used by either an employer or a student, False otherwise
    return employer_exists or student_exists


# validates logging in  for both students and employers
@app.route('/std_profile_login', methods=['POST', 'GET'])
def std_profile_login():
    if request.method == 'POST':
        #save the form data
        form = request.form
        #check if the email is in the students table
        student = Students.query.filter(func.lower(Students.email) == func.lower(form['email'])).first()
        #if the email is in the students table, check the password
        if student is not None:
            if student.check_password(form['password']):
                session["student"] = student.id
                #redirect to the student profile page
                return redirect(url_for('profileStudent'))
            else:
                #if the password is incorrect, flash an error message and redirect to the login page
                flash("password check failed")
                return render_template('login.html')
        else:
            #if the email is not in the students table, check the employers table
            form = request.form
            #check if a student is in the session, if so, remove the student from the session
            if student in session:
                for student in session:
                    del session['student']
            #check if the email is in the employers table
            employer = Employers.query.filter(func.lower(Employers.email) == func.lower(form['email'])).first()
            #if the email is in the employers table, check the password
            if employer is not None:
                #if the password is correct, add the employer to the session and redirect to the employer profile page
                if employer.check_password(form['password']):
                    session["employer"] = employer.id
                    return redirect(url_for('profileEmployer'))
                #if the password is incorrect, flash an error message and redirect to the login page
                else:
                    flash("password check failed")
                    return render_template('login.html')
            #if the email is not in the employers table, flash an error message and redirect to the login page
            else:
                print("no user found")
                return render_template('login.html')
    #if the request method is not POST, render the login page
    else:
        return render_template('createStudent.html')


# routes to the student profile page
@app.route('/profileStudent', methods=['POST', 'GET'])
def profileStudent():
    #check if the student is in the session
    if "student" in session:

        student = session["student"]
        student = Students.query.filter_by(id=student).first()
        #render the student profile page
        return render_template('profileStudent.html', student=student)
    #if the student is not in the session, redirect to the login page
    else:
        return redirect(url_for('login'))


# routes to the employer profile page
@app.route('/profileEmployer', methods=['POST', 'GET'])
def profileEmployer():
    #check if the employer is in the session
    if "employer" in session:
        employer = session["employer"]
        employer = Employers.query.filter_by(id=employer).first()
        #render the employer profile page
        return render_template('profileEmployer.html', employer=employer)
    #if the employer is not in the session, redirect to the login page
    else:
        return redirect(url_for('login'))


# route to provide a list of applicants for a job
@app.route('/job/<int:job_id>/applicants')
def job_applicants(job_id):
    # get the job from the database
    job = Jobs.query.get_or_404(job_id)
    # get the list of applicants for the job
    applicants = [application.student for application in job.applicants]
    # return the list of applicants
    applicant_data = [{'first_name': applicant.first_name, 'last_name': applicant.last_name, 'avatar': applicant.avatar,
                       'resume': applicant.resume} for applicant in applicants]
    # return the list of applicants
    return jsonify(applicant_data)


# routes to the edit student page
@app.route('/editStudent', methods=['GET', 'POST'])
def editStudent():
    #sets the avatar upload folder
    UPLOAD_FOLDER = app.config['UPLOAD_FOLDER']
    #sets the resume upload folder
    RESUME_FOLDER = app.config['RESUME_FOLDER']

    #check if the student is in the session
    if "student" in session:
        #get the student from the session
        student = session["student"]
        student = Students.query.get(student)

        #if the request method is POST
        if request.method == 'POST':
            # update student information based on form data
            student.first_name = request.form['studentfirstName']
            student.last_name = request.form['studentlastName']
            student.major = request.form['studentMajor']
            student.looking_for_job = bool(request.form.get('studentAvailability'))

            # Update email if new email is provided and not already in use
            if not student.email == request.form['studentEmail']:
                if not is_email_used(request.form['studentEmail']):
                    student.email = request.form['studentEmail']
                else:
                    flash('Email already in use', 'error')

            # Update password if new password is provided and matches confirmation and is at least 5 characters long
            new_password = request.form.get('newPassword')
            if len(new_password) >= 5:
                confirm_password = request.form.get('confirmPassword')
                if new_password and confirm_password and new_password == confirm_password:
                    student.set_password(new_password)

            # check if a new resume file is uploaded
            if 'newResume' in request.files:
                resume_file = request.files['newResume']

                #if a new resume file is uploaded
                if resume_file.filename != '':
                    #securely save the resume file on the server
                    if allowed_resume_file(resume_file.filename):
                        #generate the new resume filename
                        resume_filename = f"{student.first_name}_{student.last_name}_{student.id}_Resume.pdf"
                        #save the uploaded resume with the new name
                        resume_file.save(os.path.join(RESUME_FOLDER, secure_filename(resume_filename)))
                        #update the student's resume attribute with the new filename
                        student.resume = resume_filename
                    else:
                        # if the file format is not allowed, flash an error message and redirect to the editStudent page
                        flash('Invalid file format. Please upload a PDF file for the resume.', 'error')
                        return redirect(url_for('editStudent'))  # Redirect to editStudent route or template

            # Update avatar if a new file is uploaded
            if 'newstudentAvatar' in request.files:
                avatar_file = request.files['newstudentAvatar']
                #if a new avatar file is uploaded
                if avatar_file.filename != '':
                    #securely save the avatar file on the server
                    if allowed_file(avatar_file.filename):

                        #generate the new avatar filename
                        avatar_filename = f"{student.first_name}_{student.last_name}_{student.id}_Avatar{os.path.splitext(avatar_file.filename)[1]}"

                        # Check if there's an existing avatar file with a different extension
                        old_avatar_path = os.path.join(app.config['UPLOAD_FOLDER'],
                                                       f"{student.first_name}_{student.last_name}_{student.id}_Avatar.*")
                        old_avatar_files = glob.glob(old_avatar_path)

                        #remove the old avatar file
                        for old_avatar_file in old_avatar_files:
                            os.remove(old_avatar_file)

                        # Save the uploaded avatar with the new name
                        avatar_file.save(os.path.join(app.config['UPLOAD_FOLDER'], avatar_filename))

                        # Update the student's avatar attribute with the new filename
                        student.avatar = avatar_filename

            try:
                db.session.commit()
                return redirect(url_for('profileStudent'))
            except Exception as e:
                # Handle any exceptions that may occur during the database commit
                print(e)
        else:
            # If it's a GET request or after processing a POST request, render the template
            return render_template('editStudent.html', student=student)
    else:
        #if there is no student in the session, redirect to the login page
        return redirect(url_for('login'))  # Assuming you have a 'login' route


# routes to the edit employer page
@app.route('/editEmployer', methods=['GET', 'POST'])
def editEmployer():
    # Set the upload folder for avatar images
    UPLOAD_FOLDER = app.config['UPLOAD_FOLDER']
    # Check if the employer is in the session
    if "employer" in session:
        employer = session["employer"]
        employer = Employers.query.get(employer)

        # If the request method is POST
        if request.method == 'POST':
            # Update employer information based on form data
            employer.first_name = request.form['employerfirstName']
            employer.last_name = request.form['employerlastName']
            employer.email = request.form['employerEmail']
            employer.company_name = request.form['employerCompany']
            employer.address = request.form['employerAddress']
            employer.phone = request.form['employerPhone']

            # Update email if new email is provided and not already in use
            if not employer.email == request.form['employerEmail']:
                if not is_email_used(request.form['employerEmail']):
                    employer.email = request.form['employerEmail']
                else:
                    flash('Email already in use', 'error')

            # Update password if new password is provided and matches confirmation and is at least 5 characters long
            new_password = request.form.get('newPassword')
            if len(new_password) >= 5:
                confirm_password = request.form.get('confirmPassword')
                if new_password and confirm_password and new_password == confirm_password:
                    employer.set_password(new_password)

            # Update avatar if a new file is uploaded
            if 'newemployerAvatar' in request.files:
                avatar_file = request.files['newemployerAvatar']
                if avatar_file.filename != '':
                    # Securely save the avatar on the server
                    if allowed_file(avatar_file.filename):
                        # Generate the new avatar ename
                        avatar_filename = f"{employer.first_name}_{employer.last_name}_{employer.id}_Avatar{os.path.splitext(avatar_file.filename)[1]}"
                        #save the previous avatar name
                        previous_avatar = employer.avatar
                        # Update the employer's avatar attribute with the new filename
                        employer.avatar = avatar_filename

                        # Check if there's an existing avatar file with a different extension
                        old_avatar_path = os.path.join(app.config['UPLOAD_FOLDER'],
                                                       f"{employer.first_name}_{employer.last_name}_{employer.id}_Avatar.*")
                        old_avatar_files = glob.glob(old_avatar_path)
                        update_avatar(previous_avatar, avatar_filename)
                        # Remove the old avatar files
                        for old_avatar_file in old_avatar_files:
                            os.remove(old_avatar_file)

                        # Save the uploaded avatar with the new name
                        avatar_file.save(os.path.join(app.config['UPLOAD_FOLDER'], avatar_filename))

            # Commit the changes to the database
            try:
                db.session.commit()
                return redirect(url_for('profileEmployer'))
            except Exception as e:
                # Handle any exceptions that may occur during the database commit
                print(e)
        else:
            # If it's a GET request or after processing a POST request, render the template
            return render_template('editEmployer.html', employer=employer)
    else:
        # if there's no employer in the session, redirect to the login page
        return redirect(url_for('login'))  # Assuming you have a 'login' route


# Function to check if the uploaded avatar file has an allowed extension
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# Function to check if the uploaded resume file has an allowed extension
def allowed_resume_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'pdf', 'doc', 'docx'}


# Function to update all jobs with a new matching avatar
def update_avatar(previous_avatar, new_avatar):
    jobs_with_matching_avatar = Jobs.query.filter_by(avatar=previous_avatar).all()
    for job in jobs_with_matching_avatar:
        job.avatar = new_avatar
    db.session.commit()


# route to delete a student or employer account
@app.route('/delete_account', methods=['POST'])
def delete_account():
    # check if the student is in the session
    if 'student' in session:
        student_id = session['student']
        student = Students.query.get(student_id)

        # check if the student exists
        if student:

            # delete the student from the database
            db.session.delete(student)

            # commit the changes to the database
            db.session.commit()
            session.clear()

            # return a success message
            return render_template('home.html', message='Student deleted successfully'), 200

        # return an error message if the student does not exist
        else:
            return render_template('editStudent.html', message='Student not found'), 404

    # check if the employer is in the session
    elif 'employer' in session:
        employer_id = session['employer']
        employer = Employers.query.get(employer_id)
        # check if the employer exists
        if employer:
            #get all jobs posted by the employer
            employer_jobs = Jobs.query.filter_by(company_name=employer.company_name).all()

            #delete all jobs posted by the employer
            for job in employer_jobs:
                db.session.delete(job)

            #delete the employer from the database
            db.session.delete(employer)
            db.session.commit()
            session.clear()

            #return a success message and redirect to the home page
            return render_template('home.html', message='Employer deleted successfully'), 200

        #return an error message if the employer does not exist
        else:
            return render_template('editEmployer.html', message='Employer not found'), 404

    #return an error message if no user is logged in
    else:
        return render_template('home.html', message='no user logged in'), 401


# routes to the job listings page
@app.route('/jobListings')
def jobListings():
    # check if the student is in the session
    if "student" in session:
        student = session["student"]
        student = Students.query.filter_by(id=student).first()
        # get the 20 most recent job listings that the student has not applied to
        jobListings = db.session.query(Jobs).outerjoin(Applications, (Applications.job_id == Jobs.id) & (
                Applications.student_id == student.id)).filter(Applications.id.is_(None)).order_by(
            Jobs.date_created.desc()).limit(20).all()
        # render the job listings page
        return render_template('jobListings.html', jobs=jobListings, student=student, employers="employers")
    # check if the employer is in the session
    elif "employer" in session:
        # check if the student is in the session, if so, remove the student from the session
        if "student" in session:
            for student in session:
                del session['student']
        # get the employer from the session
        employer = session["employer"]
        employer = Employers.query.filter_by(id=employer).first()

        # get the 20 most recent job listings that the employer has posted
        if employer:
            jobListings = Jobs.query.filter_by(company_name=employer.company_name).order_by(
                Jobs.date_created.desc()).limit(20).all()
            job_applicants = {}
            # get the number of applicants for each job
            return render_template('jobListings.html', jobs=jobListings, employer=employer)
    # if neither the student nor the employer is in the session, redirect to the login page
    else:
        return redirect(url_for('login'))


# route to the job details
@app.route('/job/<int:job_id>')
def get_job_details(job_id):
    job = Jobs.query.get(job_id)
    # check if the job exists
    if job:
        # return the job details
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
        }
    # if the job does not exist, return an error message
    else:
        return {'error': 'Job not found'}, 404


# route to apply for a job
@app.route('/apply_for_job', methods=['POST'])
def apply_for_job():
    # check if the student is in the session
    if 'student' not in session:
        # redirect to login if student is not logged in
        return redirect(url_for('login'))

    #get student id from session
    student_id = session['student']

    # get the job ID from the request data
    job_id = request.json.get('job_id')

    # check if the student ID and job ID exist
    if student_id:
        if job_id:
            # get the student and job from the database
            student = Students.query.get(student_id)
            job = Jobs.query.get(job_id)

            # check if the student and job exist
            if student and job:

                # Create a new application instance
                application = Applications(student_id=student_id, job_id=job_id)

                # Add the application to the database
                db.session.add(application)
                db.session.commit()

                # Redirect to the student profile page
                return redirect(url_for('profileStudent'))
            else:
                # Return an error message if the student or job does not exist
                return jsonify({'error': 'Student or Job not found'}), 404
        else:
            # Return an error message if the job ID is missing
            return jsonify({'error': 'Job Id not found'}), 401
    else:
        # Return an error message if the student ID is missing
        return jsonify({'error': 'Student ID is missing'}), 402


# route for job filtering based on major and job type
@app.route('/filterJobs', methods=['POST'])
def filterJobs():
    # check if the student is in the session
    if 'student' in session:
        student = session['student']
        student = Students.query.filter_by(id=student).first()
        # Get the major and job type selected by the student
        major = request.form.get('Major')
        job_type = request.form.get('Hours')

        # Get all jobs from the database based on the selected major and job type
        filtered_jobs = Jobs.query
        if major and job_type:
            filtered_jobs = filtered_jobs.filter_by(major_required=major, hours=job_type)
        elif major:
            filtered_jobs = filtered_jobs.filter_by(major_required=major)
        elif job_type:
            filtered_jobs = filtered_jobs.filter_by(hours=job_type)
        # Get the filtered jobs
        filtered_jobs = filtered_jobs.all()

        # Render the job listings page with the filtered jobs
        return render_template('jobListings.html', jobs=filtered_jobs, student=student)
    # if the student is not in the session, redirect to the login page
    else:
        return redirect(url_for('login'))


# routes to the job posting page
@app.route('/postJob', methods=['GET', 'POST'])
def postJob():
    # check if the employer is in the session
    if "employer" in session:
        employer = session["employer"]
        employer = Employers.query.get(employer)

        # if the request method is POST
        if request.method == 'POST':

            # get the form data
            title = request.form['Title']
            description = request.form['Description']
            location = request.form['Address']
            deadline = request.form['Deadline']
            major_required = request.form['Major']
            pay = request.form['Pay']
            hours = request.form['Hours']

            # convert the deadline to a datetime object
            deadline_datetime = datetime.strptime(deadline, '%Y-%m-%d')

            # create a new job instance
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

            # add the job to the database
            db.session.add(job)
            db.session.commit()

            # redirect to the job listings page
            return redirect(url_for('jobListings'))
        else:
            return render_template('postJob.html', employer=employer)
    else:
        return redirect(url_for('login'))


# route to delete a job
@app.route('/delete_job', methods=['POST'])
def delete_job():
    # check if the employer is in the session
    if 'employer' in session:
        employer_id = session['employer']
        employer = Employers.query.get(employer_id)

        # get the job ID from the request data
        job_id = request.json.get('job_id')
        job = Jobs.query.get(job_id)

        # check if the job exists and the employer is the owner of the job
        if job and employer.company_name == job.company_name:

            # get all applicants for the job and delete them
            applicants = Applications.query.filter_by(job_id=job_id).all()
            for applicant in applicants:
                db.session.delete(applicant)
            db.session.delete(job)
            db.session.commit()

            # redirect to the employer profile page
            return redirect(url_for('profileEmployer'))

        # return an error message if the job does not exist or the employer is not the owner of the job
        else:
            return jsonify({'error': 'Job not found or you do not have permission to delete it'}), 404

    # return an error message if the user is not an employer
    else:
        return jsonify({'error': 'You must be logged in as an employer to delete a job'}), 401


# route to resources page
@app.route('/resources')
def resources():
    # check if the student is in the session
    if "student" in session:
        student = session["student"]
        student = Students.query.filter_by(id=student).first()
        # render the resources page
        return render_template('resources.html', student=student, employers="employers")

    # check if the employer is in the session
    elif "employer" in session:

        # check if the student is in the session, if so, remove the student from the session
        if "student" in session:
            for student in session:
                del session['student']

        # get the employer from the session
        employer = session["employer"]
        employer = Employers.query.filter_by(id=employer).first()

        # render the resources page
        return render_template('resources.html', employer=employer)

    # if neither the student nor the employer is in the session, redirect to the login page
    else:
        return redirect(url_for('login'))


# route that logs the user out
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))
