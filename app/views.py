from app import app
from flask import render_template


@app.route('/')
def index():
    return render_template("home.html")


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
