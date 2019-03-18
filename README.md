# Python CRUD Application with Django 

## Description

- This application was developed for a coding challenge, which only specified that it be a full
CRUD application written in Python using the Django framework. From the landing page, the user 
should be able to see the list of items (I went with an Avengers theme because I just saw Captain 
Marvel last weekend) and include a details page that is pathed to using the field name. The user 
should also be able to update and delete each Avenger in the list. 

- This is a full stack application, but the frontend is fairly simple, with no JavaScripts and only
basic CSS


## Resources Used
I leaned heavily on the tutorial videos from Derek Banas on Youtube to get my head around
what I was doing with setting up a Django project.
https://www.youtube.com/playlist?list=PLGLfVvz_LVvSMqZiTTsAC7C8Ypp81Jt6D

I also looked at the resource Django Girls to complete working on the update/add functionality. 
https://tutorial.djangogirls.org/en/django_forms/

## Running the Application Locally

Make sure you have the latest version of Django installed

Create the database:

    ./manage.py makemigrations
    ./manage.py migrate

Then run the server:

    ./manage.py runserver

## Heroku


