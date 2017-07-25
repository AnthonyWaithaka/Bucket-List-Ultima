# bucketlist.py
"""Activity module -
New bucketlist initialization
"""

class NewBucketList(object):
    """NewBucketList class -
    Has methods for activities management
    """
    def __init__(self, list_name, list_year, list_month, list_quote):
        self.list_name = list_name
        self.list_year = list_year
        self.list_month = list_month
        self.list_quote = list_quote
        self.activity_list = []    #activity_list will have {name:object} format

    def create_activity(self, activity_name):
        """Returns Activity object or None
        """
        for i in self.activity_list:
            if i == activity_name:
                return None
        self.activity_list.append(activity_name)
        return True

    def delete_activity(self, activity_name):
        """Delete an activity
        Return None
        """
        for i in self.activity_list:
            if i == activity_name:
                self.activity_list.remove(activity_name)
        return None

    def update_activity(self, activity_name, newname):
        """Update activity name
        Return None
        """
        for i in self.activity_list:
            if i == activity_name:
                holder = self.activity_list.index(i)
                self.activity_list[holder] = newname
        for j in self.activity_list:
            if j == activity_name:
                return False
        return None
