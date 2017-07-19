# client.py

from app.bucketlist import bluBucketList

class bluClient(object):
    def __init__(self, userName, userEmail, userPassword):
        self.userName = userName
        self.userEmail = userEmail
        self.userPassword = userPassword
        self.bL_list = {}
        self.followedLists = []


    def createBList(self, list_name, list_year, list_month, list_quote, set_active):
        for key,obj in self.bL_list.items():
            if list_name == key:
                return False
        
        #verifying that the month is not a number:
        if not list_month.isalpha():
            return False

        new_bList = bluBucketList(list_name, list_year, list_month, list_quote, set_active)
        self.bL_list.update({list_name:new_bList})
        return new_bList
    
    def viewList(self, listname):
        for key,obj in self.bL_list.items():
            if key == listname:
                return obj
        return None

    def deleteList(self, bulist):
        for key,obj in self.bL_list.items():
            if obj == bulist:
                holder = key
                del self.bL_list[holder]
                for i in list(self.bL_list.values()):
                    if i == bulist:
                        return 2
                for j in list(self.bL_list.values()):
                    if j == holder:
                        return 3
                return True
    
    def followList(self, listName):
        for i in self.followedLists:
            if listName == i:
                self.followedLists.remove(listName)
                return 2
        self.followedLists.append(listName)
        return True

    #def viewOtherList(self, bulist):
    #    bluServer.viewClient()
    # I don't think it's possible to view someone's list like this. It should be a server method