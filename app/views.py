# views.py
"""Main Program -
Data is stored in class variables
for module application
"""
from flask import render_template, redirect, url_for
from flask import request

from app import APP
from app.application import Application

NEWAPP = Application()

#@APP.route('/')
#def index():
#    """Responds to submit trigger
#    """
#    return render_template("index.html")

@APP.route('/index')
def index():
    """Sign in validation
    """
    #useremail = request.form['inpEmail']
    #userpassword = request.form['inpPass']
    #userpassword2 = request.form['inpPass2']
    #username = request.form['inpUName']
    #tnc = request.form['inpTnC']
    #operation on text
    #if Application.validate_email(useremail) and not Application.check_email_repeat(useremail):
    #    if not Application.check_password_repeat(userpassword):
    #        if userpassword == userpassword2:
    #            if not Application.check_username_repeat(username) and tnc:
    #                Application.create_user(useremail,username,userpassword,tnc)
    #                #return redirect('home.html')
    #                open('.template/home.html').read()
    return render_template('index.html')

@APP.route('/signup/', methods=['POST'])
def sign_up():
    if request.form['submit'] == 'Sign Up':
        #useremail = request.form['email']
        #result = NEWAPP.check_email_repeat(useremail)
        return redirect(url_for('home'))
    return render_template('index.html')

@APP.route('/home')
def home():
    """Home Page -
    """
    return render_template("home.html")
