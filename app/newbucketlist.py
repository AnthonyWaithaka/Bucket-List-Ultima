# bucketlist.py
"""Activity module -
New bucketlist initialization
"""

class NewBucketList(object):
    """BucketList class -
    Has methods for bucketlist management
    """
    def __init__(self, list_name, list_year, list_month, list_quote, set_active):
        self.list_name = list_name
        self.list_year = list_year
        self.list_month = list_month
        self.list_quote = list_quote
        self.set_active = set_active
        self.activity_list = {}    #activity_list will have {name:object} format

    def create_activity(self, activity_name, media_path_list, achieved_status):
        """Creates a new activity and stores it
        """
        for i in list(self.activity_list.keys()):
            if i == activity_name:
                return None
        new_activity = Activity(activity_name, media_path_list, achieved_status)
        self.activity_list.update({activity_name:new_activity})
        return new_activity

    def view_activity(self, activity_name, *args):
        """Given an activity name as argument
        and a property type
        Returns the respective property type data
        """
        for i in list(self.activity_list.keys()):
            if i == activity_name:
                for arg in args:
                    if arg == 'media_list':
                        return self.activity_list[activity_name].media_path_list
                    elif arg == 'status':
                        return self.activity_list[activity_name].status_
        return None

    def edit_status(self, activity_name):
        """Given an activity name as argument
        Can edit the achieved status of
        the respective activity object
        """
        for i in list(self.activity_list.keys()):
            if i == activity_name:
                self.activity_list[activity_name].flip_status()
        return None

    def delete_activity(self, activity_name):
        """Deletes an activity
        """
        for i in list(self.activity_list.keys()):
            if i == activity_name:
                del self.activity_list[activity_name]
        return None

    def reset_activity(self, activity_name, newname):
        """Reset activity name
        """
        for i in list(self.activity_list.keys()):
            if i == activity_name:
                self.activity_list[newname] = self.activity_list.pop(activity_name)
                self.activity_list[newname].activity_name = newname

class Activity(object):
    """Activity Class -
    Methods are file handling
    """
    def __init__(self, activity_name, media_path_list, status_):
        self.activity_name = activity_name
        self.media_path_list = media_path_list
        self.status_ = status_

    def flip_status(self):
        """Changes the status from true
        to false and vice versa
        """
        self.status_ = not self.status_
        return None

    def add_media(self, path_name):
        """Adds a media path to the list
        """
        self.media_path_list.append(path_name)
        return None

    def remove_media(self, path_name):
        """Removes media path from list
        """
        for i in self.media_path_list:
            if i == path_name:
                self.media_path_list.remove(path_name)
        return None
