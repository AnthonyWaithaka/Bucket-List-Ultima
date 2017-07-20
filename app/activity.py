# activity.py
"""Activity module -
See documentation for use
"""

class Activity(object):
    """Activity Class -
    Methods are file handling
    """
    def __init__(self, activity_name, media_path_list, achievement_status):
        self.activity_name = activity_name
        self.media_path_list = media_path_list
        self.achievement_status  = achievement_status