# Welcome to Backend for IOT Project!

The project is for making a basic **UI** and application for registering sensors and displaying their data.

The application will perform basic **CRUD** operation.


# Technology Used
The technology used for building the backend is **Django**.
and **Django-rest-framework** is also used.

***Django is a high-level Python web framework*** that encourages rapid development and clean, pragmatic design. Built by experienced developers, it takes care of much of the hassle of web development, so you can focus on writing your app without needing to reinvent the wheel. It’s free and open source.


## Installations

 - [ ] 1st we created a virtual environment inside a folder in order to
       install all the basic dependencies inside the project directory
       only.

Creating a virtual environment:

    python -m venv <foldername>

Then we installed the modules used using **pip** command

    pip install django

    pip install django-rest-framework

## Starting the Server

In order to tart the server we need to run the django commands.

1st we have to create a database, we can do it by using the following commands:

    python manage.py makemigrations

    python manage.py migrate

The *makemigrations* command will detect and stage all the changes which are necessary to be updated to the database.
And finally the *migrate*command will update those changes in the database.
Initially these two commands will create the database.

We have inbuild database support in Django. 
The database used by django by default is **SQLite3.**

After the database is created we need to create a superuser to access the Admin pannel. for it we use the command below

    python manage.py createsuperuser 

And finally for starting the server we use the below command:

    python manage.py runserver

running this command will start the server in your local machine in **8000** port number.

## Hosted Backend

The backend is hosted in the following website provided below.

### [Click me](https://hasibnirban.pythonanywhere.com/)
