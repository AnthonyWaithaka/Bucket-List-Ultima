# app/application.py
"""Methods for registering users
and keeping records
"""

import re
from .bucketlists import BucketLists

class Application(object):
    """Application is not meant to have
    instances but to reference methods
    and class variables
    """
    EMAIL_LIST = []
    PASSWORD_LIST = []
    USERNAME_LIST = []
    USER_LIST = {}
    ACCESS_LIST = {}
    def __init__(self):
        pass

    def validate_email(self, user_email):
        """Return email for valid email address format.
        Return false otherwise
        """
        match = re.match(
            '^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$',
            user_email)

        if match is None:
            return False
        else:
            return user_email

    def check_email_repeat(self, user_email):
        """Return True for existing email address record
        """
        checker = False
        for i in self.EMAIL_LIST:
            if i == user_email:
                checker = True
                return checker
        return checker

    def check_password_repeat(self, user_password):
        """Checks if existing password record
        """
        checker = False
        for i in self.PASSWORD_LIST:
            if i == user_password:
                checker = True
                return checker
        return checker

    def check_username_repeat(self, user_name):
        """Checks for existing username record
        """
        checker = False
        for i in self.USERNAME_LIST:
            if i == user_name:
                checker = True
                return checker
        return checker

    def create_user(self, user_email, user_name, user_password, terms_and_conditions):
        """Create BucketLists object initialized
        to the user's data
        """
        new_user_email = self.validate_email(user_email)

        if not terms_and_conditions:
            return None

        if not self.validate_email(user_email):
            return None

        if self.check_email_repeat(new_user_email):
            return None

        if self.check_password_repeat(user_password):
            return None

        if self.check_username_repeat(user_name):
            return None

        self.EMAIL_LIST.append(new_user_email)

        self.PASSWORD_LIST.append(user_password)

        self.USERNAME_LIST.append(user_name)

        self.USER_LIST.update({user_name:(new_user_email, user_password)})

        #create a user's bucketlist group initialized with user_id, email_address and pwd
        new_user = BucketLists(user_name, new_user_email, user_password)

        #add user_id and associated object to ACCESS_LIST
        self.ACCESS_LIST.update({user_name:new_user})

        #return the new user object
        return new_user

    def delete_user(self, username):
        """Delete user's BucketLists object and scan
        for remnant data. Returns True for error
        and None for no error
        """
        for key in list(self.ACCESS_LIST.keys()):
            checker = None
            if key == username:
                holder = self.USER_LIST[key]    #holder is (email,pwd)
                self.USERNAME_LIST.remove(key)
                self.EMAIL_LIST.remove(holder[0])
                self.PASSWORD_LIST.remove(holder[1])
                del self.ACCESS_LIST[key]
                del self.USER_LIST[key]

                for j in self.USERNAME_LIST:
                    if j == key:
                        checker = True
                for k in self.EMAIL_LIST:
                    if k == holder[0]:
                        checker = True
                for pwd in self.PASSWORD_LIST:
                    if pwd == holder[1]:
                        checker = True
                for userid in list(self.ACCESS_LIST.values()):
                    if userid == key:
                        checker = True
                for username in list(self.USER_LIST.keys()):
                    if username == key:
                        checker = True
            return checker

    def view_user(self, username):
        """Find bucketlists with username
        """
        for i in self.USERNAME_LIST:
            if username == i:
                holder = self.ACCESS_LIST[username]
                return list(holder.bucket_lists.values())
        return None

    def view_bucket_list(self, listname, username):
        """Find a user's bucket lists from username
        """
        holder = self.ACCESS_LIST[username]
        if holder.view_list(listname) != None:
            return holder.view_list(listname)
        return None

    def search_user(self, useremail):
        """Find username from email
        """
        for i in self.USERNAME_LIST:
            holder = self.USER_LIST[i]
            if holder[0] == useremail:
                return i
        return None

    def reset_user(self, username, **kwargs):
        """Reset user's data:
        1. username
        2. useremail
        3. userpassword
        """
        newusername = kwargs.get('newusername', None)
        oldpassword = kwargs.get('oldpassword', None)
        newpassword = kwargs.get('newpassword', None)
        oldemail = kwargs.get('oldemail', None)
        newemail = kwargs.get('newemail', None)
        checker_email = False
        checker_password = False
        checker_username = False

        if newemail is not None and oldemail is not None:
            if self.check_email_repeat(oldemail) is True:
                if self.check_email_repeat(newemail) is not True:
                    holder = self.USERNAME_LIST.index(oldemail)
                    self.EMAIL_LIST[holder] = newemail
                    self.ACCESS_LIST[username][0] = newemail
                    self.ACCESS_LIST[username].user_email = newemail
                    checker_email = self.check_email_repeat(oldemail)

        if  oldpassword is not None and newpassword is not None:
            if self.check_password_repeat(oldpassword) is True:
                if self.check_password_repeat(newpassword) is not True:
                    holder = self.PASSWORD_LIST.index(oldpassword)
                    self.PASSWORD_LIST[holder] = newpassword
                    self.USER_LIST[username][1] = newpassword
                    self.ACCESS_LIST[username].user_password = newpassword
                    checker_password = self.check_password_repeat(oldpassword)

        if newusername is not None:
            if self.check_username_repeat(username) is True:
                if self.check_username_repeat(newusername) is not True:
                    holder = self.USERNAME_LIST.index(username)
                    self.USERNAME_LIST[holder] = newusername
                    self.USER_LIST[newusername] = self.USER_LIST.pop(username)
                    self.ACCESS_LIST[newusername] = self.ACCESS_LIST.pop(username)
                    self.ACCESS_LIST[newusername].user_name = newusername
                    checker_username = self.check_username_repeat(username)

        if checker_email or checker_password or checker_username:
            return False

        return None
