# views.py
"""Main Program -
Data is stored in class variables
for module application
"""
import datetime
from datetime import date

from flask import render_template, redirect, session
from flask import request, url_for

from app import APP
from app.application import Application

NEWAPP = Application()
now = datetime.datetime.now()

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
                        return render_template('index.html', pageType="login")
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
    session['loginuser'] = None
    if NEWAPP.validate_email(email) is False:
        if NEWAPP.check_username_repeat(email) is True:
            #check that password matches username
            if NEWAPP.USER_LIST[email][1] == password:
                session['loginuser'] = email  #store username in session cache
                return redirect(url_for('bucketlists'))
            else:
                message = "Wrong username/password"
        else:
            message = "Username is not in records"
    else:
        if NEWAPP.check_email_repeat(email) is True:
            #check that password matches email
            loguser = NEWAPP.search_user(email)
            if NEWAPP.USER_LIST[loguser][1] == password:
                session['loginuser'] = loguser  #store username in session cache
                return redirect(url_for('bucketlists'))
            else:
                message = "Wrong email/password"
        else:
            message = "Email is not in records"
    return render_template('index.html', pageType="login", message2=message)

@APP.route('/mylists', methods=['GET', 'POST'])
def bucketlists():
    """BucketLists page
    """
    if session['loginuser']:
        username = session['loginuser']
    else:
        return redirect(url_for('log_in'))
    #Return session user's bucketlists
    sessionblist = []
    deadline = []
    useralist = []
    useralistdict = {}
    userblist = list(NEWAPP.ACCESS_LIST[username].bucket_lists.keys())
    if userblist is not None:
        for key in userblist:
            sessionblist.append(NEWAPP.ACCESS_LIST[username].bucket_lists[key])
            useralist = (list(NEWAPP.ACCESS_LIST[username].bucket_lists[key].activity_list))
            useralistdict.update({key:useralist})
            date_one = date(NEWAPP.ACCESS_LIST[username].bucket_lists[key].list_year,
                            NEWAPP.ACCESS_LIST[username].bucket_lists[key].list_month, 1)
            date_two = date(now.year, now.month, 1)
            delta = date_one - date_two
            if delta.days < 0:
                deadline.append("deadline passed")
            else:
                deadline.append(delta.days)
    else:
        sessionblist = 0
    #Return session user's data in pieces for: list of (list of) bucketlist names,
    # list of (list of) activities
    userdata = dict(zip(userblist, sessionblist)) #dict of bucketlist names and bucketlist objects
    userdeadline = dict(zip(userblist, deadline)) #dict of bucketlist names and deadlines
    return render_template("MyLists.html", title=username, user=username,
                           userblist=userblist, sessionblist=sessionblist,
                           userdata=userdata, userdeadline=userdeadline,
                           useralistdict = useralistdict)

@APP.route('/newlist', methods=['GET', 'POST'])
def new_list():
    """Bucketlists page
    New list method
    """
    username = session['loginuser']
    newlistname = request.form['newlistname']
    listyear = int(request.form['list_year'])
    listmonth = int(request.form['list_month'])
    listquote = request.form['list_quote']
    if username is not None:
        if listyear != 0 and listmonth != 0:
            NEWAPP.ACCESS_LIST[username].create_bucket_list(newlistname,
                                                            listyear,
                                                            listmonth, listquote)
            return redirect(url_for('bucketlists'))
        else:
            return redirect(url_for('bucketlists'))
    else:
        return redirect(url_for('log_in'))

@APP.route('/deletelist/', methods=['GET', 'POST'])
def delete_list():
    listnametodelete = request.form['listtodelete']
    usernametodelete = session['loginuser']
    NEWAPP.ACCESS_LIST[usernametodelete].delete_list(listnametodelete)
    return redirect(url_for('bucketlists'))

@APP.route('/editlist/', methods=['GET', 'POST'])
def edit_list():
    listnametoedit = request.form.get('listtoedit')
    username = session['loginuser']
    newlistname = request.form['newbname']
    newlistquote = request.form['newbquote']
    listyear = int(request.form['editlist_year'])
    listmonth = int(request.form['editlist_month'])
    if newlistname:
        NEWAPP.ACCESS_LIST[username].update_bucketlist(listnametoedit, newlistname=newlistname)
    if newlistquote:
        NEWAPP.ACCESS_LIST[username].update_bucketlist(listnametoedit, quote=newlistquote)
    if listyear != 0:
        NEWAPP.ACCESS_LIST[username].update_bucketlist(listnametoedit, year=listyear)
    if listmonth != 0:
        NEWAPP.ACCESS_LIST[username].update_bucketlist(listnametoedit, month=listmonth)
    return redirect(url_for('bucketlists'))

@APP.route('/addactivity/', methods=['GET', 'POST'])
def add_activity():
    listtoedit = request.form.get('listtoupdate')
    usertoedit = session['loginuser']
    newactivity = request.form['newactivity']
    NEWAPP.ACCESS_LIST[usertoedit].bucket_lists[listtoedit].create_activity(newactivity)
    return redirect(url_for('bucketlists'))

@APP.route('/editactivity/', methods=['GET', 'POST'])
def edit_activity():
    listtoedit = request.form.get('blisttoedit')
    usertoedit = session['loginuser']
    newname = request.form['newaname']
    aname = request.form.get('currentactivity')
    NEWAPP.ACCESS_LIST[usertoedit].bucket_lists[listtoedit].update_activity(aname, newname)
    return redirect(url_for('bucketlists'))

@APP.route('/deleteactivity/', methods=['GET', 'POST'])
def delete_activity():
    listtoedit = request.form.get('blisttodelete')
    usertoedit = session['loginuser']
    delname = request.form.get('atodelete')
    NEWAPP.ACCESS_LIST[usertoedit].bucket_lists[listtoedit].delete_activity(delname)
    return redirect(url_for('bucketlists'))

@APP.route('/settings')
def settings():
    username = session['loginuser']
    return render_template('settings.html', title=username, useremail=NEWAPP.USER_LIST[username][0])

@APP.route('/settings/', methods=['GET', 'POST'])
def edit_settings():
    username = session['loginuser']
    newusername = request.form['newusername']
    newemail = request.form['newemail']
    newpassword = request.form['newpassword']

    if newpassword:
        NEWAPP.reset_user(username, newpassword=newpassword,
                          oldpassword=NEWAPP.USER_LIST[username][1])
    if newemail:
        NEWAPP.reset_user(username, newemail=newemail,
                          oldemail=NEWAPP.USER_LIST[username][0])
    if newusername:
        NEWAPP.reset_user(username, newusername=newusername)
        session['loginuser'] = newusername
    return redirect(url_for('settings'))
