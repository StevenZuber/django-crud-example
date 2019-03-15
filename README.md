# Currently a WIP

##Description

- This application was developed for a coding challenge, which only specified that it be a full
CRUD application written in Python using the Django framework. From the landing page, the user 
should be able to see the list of items (I went with an Avengers theme because I just saw Captain 
Marvel last weekend) and include a details page that is pathed to using the field name. The user 
should also be able to update and delete each Avenger in the list. 

- This is a full stack application, but the frontend is fairly simple, with no JavaScripts and only
basic CSS

##Technical Choices and Architecture 
<!--
-	Reasoning behind your technical choices, including architecture.
-	Trade-offs you might have made, anything you left out, or what you might do differently if you were to spend additional time on the project.
-->

# Running the Applications

Make sure you have the latest version of Django installed

Create the database:

    ./manage.py makemigrations
    ./manage.py migrate

Then run the server:

    ./manage.py runserver

## I will deploy this on Heroku and add a link to the app when it's finished

