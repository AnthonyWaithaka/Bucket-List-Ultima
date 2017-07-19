# server.py

import re
from app.client import bluClient

client_email_list = []
client_password_list = []
client_id_list = []
client_list = {}
client_access_list = {}

class bluServer(object):
    
    def __init__(self):
        pass
    
    def validateEmail(self, userEmail):
        global client_email_list
        global client_email_counter
        match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', userEmail)

        if match == None and match.isalpha():
            return False
        else:
            return userEmail

    def checkEmailRepeat(self, userEmail):
        global client_email_list
        
        checker = False
        for i in client_email_list:
            if i == userEmail:
                checker = True
                return checker
        return checker
    
    def checkPasswordRepeat(self, userPassword):
        global client_password_list
        
        checker = False
        for i in client_password_list:
            if i == userPassword:
                checker = True
                return checker
        return checker

    def checkUsernameRepeat(self, userName):
        global client_id_list

        checker = False
        for i in client_id_list:
            if i == userName:
                checker = True
                return checker
        return checker

    def createClient(self, userEmail, userName, userPassword, terms_and_conditions):
        global client_list
        global client_email_counter
        global client_email_list
        global client_id_list
        global client_password_counter
        global client_password_list

        if terms_and_conditions is False:
            return 1
        
        new_user_email = self.validateEmail(userEmail)
        
        if new_user_email is False:
            return 2

        if self.checkEmailRepeat(new_user_email) is True:
            return 3

        if self.checkPasswordRepeat(userPassword) is True:
            return 4

        if self.checkUsernameRepeat(userName) is True:
            return 5

        client_email_list.append(userEmail)

        client_password_list.append(userPassword)
        
        client_id_list.append(userName)

        client_list.update({userName:(userEmail,userPassword)})

        #create a client object initialized with client_id, email_address and pwd
        newClient = bluClient(userName, userEmail, userPassword)

        #add client_id and associated object to client_access_list
        client_access_list.update({userName:newClient})

        #return the new client object
        return newClient

    def deleteClient(self, bluclient):        
        for key,obj in client_access_list.items():
            if obj == bluclient: #bluclient is object
                holder = client_list[key] #holder is (email,pwd)
                client_id_list.remove(key)
                client_email_list.remove(holder[0])
                client_password_list.remove(holder[1])
                del client_access_list[key]
                del client_list[key]
                for j in client_id_list:
                    if j == key:
                        return 2
                for k in client_email_list:
                    if k == holder[0]:
                        return 3
                for l in client_password_list:
                    if l == holder[1]:
                        return 3
                for m in list(client_access_list.values()):
                    if m == key:
                        return 3
                for n in list(client_list.keys()):
                    if n == key:
                        return 3
                return True
            return 2

    def viewClient(self, username):
        for i in client_id_list:
            if username == i:
                holder = client_access_list[username]
                return list(holder.bL_list.values())
        return 1

    def viewbList(self, listname, username):
        holder = client_access_list[username]
        if holder.viewList(listname) != None:
            return holder.viewList(listname)
        return None

    def searchClient(self, useremail):
        for i in client_id_list:
            holder = client_list[i]
            if holder[0] == useremail:
                return i
        return False