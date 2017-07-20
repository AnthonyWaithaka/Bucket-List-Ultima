# activity.py
"""Activity module -
See documentation for use
"""

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
