# Mywebcode Django Blog
# This is a full-featured Blog application made completely with Python Django, Bootstrap Template Use
# Visit Our Blog https://www.mywebcode.com/

This Blogging web application project is purely made with Django as the backend and Bootstrap as the frontend.

## Installation Instructions

If you want to work with this project or create a version of it make sure to follow the steps below!

0. Make sure to install ` Python 3 `, ` pip ` and ` virtualenv `   
1. Create a project folder
   
    ```bash
        $ mkdir project
        $ cd project
    ```
2. Create a python 3 virtualenv, and activate the environment to install requirements.
    ```bash
        $ python -m venv env
        $ source env/bin/activate
    ``` 
3. Install the project dependencies from `requirements.txt`
    ```
        (env)$ pip install -r requirements.txt
    ```
4. Clone the repository
   
    ```bash
        (env)$ git clone https://github.com/dydevops/Mywebcode_Django_Blog.git
        (env)$ cd Mywebcode_Django_Blog
    ```

You have now successfully set up the project on your environment.

## How to run  the project?

Make sure you are in `env` and then do the following each at a time.

```bash
(env)$ python manage.py makemigrations
(env)$ python manage.py makemigrations blog
(env)$ python manage.py makemigrations accounts
(env)$ python manage.py makemigrations pages
(env)$ python manage.py migrate
(env)$ python manage.py createsuperuser
(env)$ python manage.py runserver
```

## Features

### Blog list View
List all blog posts with Title, Tag, Number of total comments(working on for v1.2), Author Name, Date Posted, Image, and some body part with Read More button.

### Recent Posts
List all the post which are created recently with Image thumb and Title.

### category list
List all the categories related to the posts with total number of posts each categories have.

### Search
List all blog posts with the search query that you enter.

### Pagination
To limit with a certain number of posts in each page.

### Blog Detail View
To view the complete blog post when clicked on Read More or on the Title.

## Features for v1.2

### Login/Register
Users can Login/Register to the Blog App.

### Comment
Users can comment and reply to any blog post after login.

### Create Blog Post
Users can create blog posts from the front end and add for approval, by the admin.

### Edit Profile
Users can edit Profile Image, First Name, Last Name, Email id, username, password.

## Tech Stacks

* **Language:**  Python 3.9
* **Framework:** Django==4.0

## Latest Fixes

1. Added Unique Slug Generator based on Title
2. Dynamic Title Tag for Blog Details

## How you can contribute to this project?

1. Fork this project to your GitHub account
2. Clone the repository to your local machine and follow the above Installation instructions.
3. Find an issue or feature and work on it.
4. Make a pull request.
