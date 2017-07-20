# server.py
"""Server module -
See documentation for use
"""

import re
from app.client import Client

class Server(object):
    """Server class -
    Contains the main app management
    variables and functions
    """
    client_email_list = []
    client_password_list = []
    client_id_list = []
    client_list = {}
    client_access_list = {}

    def __init__(self):
        pass

    def validate_email(self, user_email):
        """Checks that input email address
        is a string in standard format
        """
        match = re.match(
            '^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$',
            user_email)

        if match is None:
            return False
        else:
            return user_email

    def check_email_repeat(self, user_email):
        """Checks if the input email address
        already exists in the record
        """
        checker = False
        for i in self.client_email_list:
            if i == user_email:
                checker = True
                return checker
        return checker

    def check_password_repeat(self, user_password):
        """Checks if the input password
        aready exists in the record
        """
        checker = False
        for i in self.client_password_list:
            if i == user_password:
                checker = True
                return checker
        return checker

    def check_username_repeat(self, user_name):
        """Checks if the input username
        already exists in the record
        """
        checker = False
        for i in self.client_id_list:
            if i == user_name:
                checker = True
                return checker
        return checker

    def create_client(self, user_email, user_name, user_password, terms_and_conditions):
        """Creates a Client object initialized
        to the input data
        """
        new_user_email = self.validate_email(user_email)

        if not terms_and_conditions:
            return None

        if self.check_email_repeat(new_user_email):
            return None

        if self.check_password_repeat(user_password):
            return None

        if self.check_username_repeat(user_name):
            return None

        self.client_email_list.append(new_user_email)

        self.client_password_list.append(user_password)

        self.client_id_list.append(user_name)

        self.client_list.update({user_name:(new_user_email, user_password)})

        #create a client object initialized with client_id, email_address and pwd
        new_client = Client(user_name, new_user_email, user_password)

        #add client_id and associated object to client_access_list
        self.client_access_list.update({user_name:new_client})

        #return the new client object
        return new_client

    def delete_client(self, clientname):
        """Deletes a Client object and scans
        for remnant data. Returns True for error
        and None for no error
        """
        for key in list(self.client_access_list.keys()):
            checker = None
            if key == clientname:
                holder = self.client_list[key]    #holder is (email,pwd)
                self.client_id_list.remove(key)
                self.client_email_list.remove(holder[0])
                self.client_password_list.remove(holder[1])
                del self.client_access_list[key]
                del self.client_list[key]

                for j in self.client_id_list:
                    if j == key:
                        checker = True
                for k in self.client_email_list:
                    if k == holder[0]:
                        checker = True
                for pwd in self.client_password_list:
                    if pwd == holder[1]:
                        checker = True
                for clientid in list(self.client_access_list.values()):
                    if clientid == key:
                        checker = True
                for clientname in list(self.client_list.keys()):
                    if clientname == key:
                        checker = True
            return checker

    def view_client(self, username):
        """Use a client's username
        to return an unsorted list
        of their bucket lists or None
        """
        for i in self.client_id_list:
            if username == i:
                holder = self.client_access_list[username]
                return list(holder.bucket_lists.values())
        return None

    def view_bucket_list(self, listname, username):
        """Uses a bucket list name and username
        to return the bucket list object or None
        """
        holder = self.client_access_list[username]
        if holder.view_list(listname) != None:
            return holder.view_list(listname)
        return None

    def search_client(self, useremail):
        """Uses a useremail to return
        a username or None
        """
        for i in self.client_id_list:
            holder = self.client_list[i]
            if holder[0] == useremail:
                return i
        return None

    def reset_client(self, username, **kwargs):
        """Resets any of the following of clients object's data:
        1. client username
        2. client useremail
        3. client userpassword
        """
        newusername = kwargs.get('newusername', None)
        oldpassword = kwargs.get('oldpassword', None)
        newpassword = kwargs.get('newpassword', None)
        oldemail = kwargs.get('oldemail', None)
        newemail = kwargs.get('newemail', None)
        checker_email = False
        checker_password = False
        checker_username = False
        if newusername is not None:
            if self.check_username_repeat(username) is True:
                if self.check_username_repeat(newusername) is not True:
                    holder = self.client_id_list.index(username)
                    self.client_id_list[holder] = newusername
                    self.client_list[newusername] = self.client_list.pop(username)
                    self.client_access_list[newusername] = self.client_access_list.pop(username)
                    self.client_access_list[newusername].reset_username(newusername)
                    checker_username = self.check_username_repeat(username)

        if newemail is not None and oldemail is not None:
            if self.check_email_repeat(oldemail) is True:
                if self.check_email_repeat(newemail) is not True:
                    holder = self.client_id_list.index(oldemail)
                    self.client_email_list[holder] = newemail
                    self.client_access_list[username][0] = newemail
                    self.client_access_list[username].reset_useremail(newemail)
                    checker_email = self.check_email_repeat(oldemail)

        if  oldpassword is not None and newpassword is not None:
            if self.check_password_repeat(oldpassword) is True:
                if self.check_password_repeat(newpassword) is not True:
                    holder = self.client_password_list.index(oldpassword)
                    self.client_password_list[holder] = newpassword
                    self.client_list[username][1] = newpassword
                    self.client_access_list[username].reset_userpassword(newpassword)
                    checker_password = self.check_password_repeat(oldpassword)

        if checker_email or checker_password or checker_username:
            return False

        return None
