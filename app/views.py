# views.py
"""Main Program -
Data is stored in class variables
for module application
"""
from flask import render_template, redirect, session
from flask import request

from app import APP
from app.application import Application

USER = Application()

@APP.route('/')
def index():
    """Index page render
    """
    return render_template('index.html')

@APP.route('/signupfailed/', methods=['GET','POST'])
def sign_up():
    """Register a new user
    """
    if request.form['submit'] == 'Sign Up':
        tnc = False
        useremail = request.form['email']
        userpassword = request.form['pass']
        userpassword2 = request.form['pass2']
        username = request.form['user']
        tnc = request.form['TnC']

        if tnc is not True:
            return render_template('index.html', message="You must accept terms and conditions")

        #operation on input
        if userpassword == userpassword2:
            if USER.create_user(useremail, username, userpassword, tnc) is not None:
                session['newuser'] = username
                return redirect('home')
            else:
                return render_template('index.html', message="Cannot create new account")
        else:
            return render_template('index.html', message="Password already exists")
    else:
        return render_template('index.html', message="Username/Email already exists")

@APP.route('<user>/home')
def home():
    """Home Page
    """
    user = session['newuser']
    return render_template('home.html')

@APP.route('/bucketlists')
def bucketlists():
    """BucketList Management Page
    """
    return render_template('MyLists.html')

@APP.route('/following')
def following():
    """Following Page
    """
    return render_template('Following.html')
