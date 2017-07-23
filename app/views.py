# views.py
"""Main Program -
Data is stored in class variables
for module application
"""
from flask import render_template, flash, redirect, session
from flask import request, url_for

from app import APP
from app.application import Application
from .forms import SignUpForm

NEWAPP = Application()

@APP.route('/', methods=['GET', 'POST'])
def index():
    """Index page render
    """
    return render_template('index.html', pageType="index")

@APP.route('/signup/', methods=['GET', 'POST'])
def sign_up():
    """Register user
    """
    email = request.form['email']
    username = request.form['user']
    password = request.form['pass']
    password2 = request.form['pass2']

    if password == password2:
        #Verify email, username and password here
        if NEWAPP.check_email_repeat(email) is False:
            if NEWAPP.check_username_repeat(username) is False:
                if NEWAPP.check_password_repeat(password) is False:
                    new_user = NEWAPP.create_user(email, username, password, True)
                    if new_user is not None:
                        session['loginuser'] = username
                        return redirect(url_for('home'))
                    else:
                        message = "Could not create account. Email not valid."
                else:
                    message = "Password is already in use"
            else:
                message = "Username is already in use"
        else:
            message = "Email is already in use"
    else:
        message = "Passwords do not match"
    return render_template('index.html', pageType="signup", message=message)

@APP.route('/login/', methods=['GET', 'POST'])
def log_in():
    """Login user
    """
    email = request.form['logemail']
    password = request.form['logpassword']
    
    if NEWAPP.validate_email(email) is False:
        if NEWAPP.check_username_repeat(email) is True:
            #check that password matches username
            if NEWAPP.USER_LIST[email][1] == password:
                session['loginuser'] = email
                return redirect(url_for('home'))
            else:
                message = "Wrong username/password"
        else:
            message = "Username is not in records"
    else:
        if NEWAPP.check_email_repeat(email) is True:
            #check that password matches email
            loguser = NEWAPP.search_user(email)
            if NEWAPP.USER_LIST[loguser][1] == password:
                session['loginuser'] = email
                return redirect(url_for('home'))
            else:
                message = "Wrong email/password"
        else:
            message = "Email is not in records"
    return render_template('index.html', pageType="login", message2=message)

@APP.route('/home')
def home():
    """Home page
    """
    return render_template('home.html')

@APP.route('/mylists')
def bucketlists():
    """BucketLists page
    """
    return render_template("MyLists.html")

@APP.route('/following')
def following():
    """Following page
    """
    return render_template("Following.html")