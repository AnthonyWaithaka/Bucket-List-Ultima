
# Bucket-List-Ultima
An application to plan, record and share achievements/experiences

Features of the release version:
1. Users can create a personal account and log in from the internet
2. Users can access an offline version of their account
3. Users with accounts can create bucket-lists, add activities to them and manipulate both
4. Users with accounts can attach media files to each activity
5. Users can view bucket lists with status 'active' and their media files
6. Users with accounts can comment on activities of bucket lists with status 'active'

The file "index.html" contains the landing page of the UI layout. It has the following features:
1. Introductory title and picture slideshow
2. A navigation bar to:
    2.1 Reload the page
    2.2 Access #3
    2.3 Access #4
3. A form to accept input and create a new user account
4. A form to accept input and log in to an existing user account
5. A placeholder document for legal purposes

The file "user/home.html" contains the main interactive page with the following features:
1. A landing with update notifications about followed bucket lists and new comments to user's bucket lists
2. A navigation bar to:
    2.1 Reload the page
    2.2 Access #3
    2.3 Access #4
    2.4 Do a search
    2.5 Access #5
3. A link to "user/MyLists.html"
4. A link to "user/Following.html" 
5. A tab where the user can:
    5.1 View account profile
        5.1.1 Change account username
        5.1.2 Change account password
        5.1.3 Change account picture
    

The file "user/MyLists.html" has the following features:
1. View all bucket lists
2. Add a bucket list
3. Remove a bucket list
4. Change bucket list status between active and inactive
5. View the number of user accounts following a bucket list
6. View all activities inside a bucket list
7. Add an activity inside a bucket list
8. Remove an activity from a bucket list
9. View all media files inside an activity
10. Add a media file inside an activity
11. Remove a media file from an activity
12. View comment history inside an activity
13. Make comments inside an activity

The file "user/Following.html" has the following features:
1. Browse other user accounts' "active" bucket lists, their activities and their media files
2. Activate "follow" on other user accounts' "active" bucket lists
3. View "followed" bucket lists
4. "Unfollow" bucket lists
5. Comment on other user accounts' "active" bucket list
