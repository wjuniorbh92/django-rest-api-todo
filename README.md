# django-rest-api-todo

This is a Backend for a Todo Application using Django Rest Api and Token Auth.

A deploy was made of this backend in Heroku and you can access the routes through the link below.
[backend-link](https://django-rest-api-todo.herokuapp.com/api/)
  

## Prerequisites

 1. Python 3 
 2.  Pip

## How to run
To start the project it is ideal to have a virtualEnv, just run the command's in the terminal.
```
pip install virtualenv
python3 -m virtualenv venv
source venv/bin/activate  **(Linux or macOS)**  
venv/Scripts/Activate  
```
With the virtual env created and activated, just install the requirements, migrate the database and run the server

```
pip install -r requirements.txt
python manage.py makemigration
python manage.py migration
python manage.py runserver
``` 

## Authentication
As per the tutorial in the token authentication documentation, to authenticate.

> For clients to authenticate, the token key should be included in the  Authorization HTTP header. The key should be prefixed by the string literal "Token", with whitespace separating the two strings. For example:
>``` Authorization: Token 944b09199c62bcf9418ad846dd0e4bbdfc6ee4b ```

And pass you authenticate yourself, you need:

> The  `curl`  command line tool may be useful for testing token authenticated APIs. For example:
>
> `curl -X GET http://127.0.0.1:8000/api/example/ -H 'Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b'`

### EndPoints
| Route | Description |  Need Pass Token| Method|
|--|--|--| --|
| api/create/ | Create a new task | Yes | POST|
| api/task-list/ | View all tasks for this user | Yes | GET |
| api/task/id/ | Details of a task with a specific id | Yes | GET |
| api/delete/ | Delete a task by passing an id | Yes |DELETE |
| api/edit/ |Edit task with specific id| Yes | PATH|
| api/login/ | Pass the username and password, and the token is returned | No | POST |
| api/register/ |Register a user by passing username and password  | No | POST |


# Deploy

I created a brach called deploy heroku, to put all the settings, please do a gitclone in Brach Deploy, if you want to test the deploy on Heroku.

## Why Heroku?
Heroku, besides being free, Heroku has a cli tool, very similar to Google Cloud and Azure, the app is already scale-ready.

## How to do deploy?

Following the tutorial on the service page, it does not leave us with many doubts.
[Heroku Tutorial Python](https://devcenter.heroku.com/articles/getting-started-with-python?singlepage=true)
If you have Error in CollectStatic, just go to WebApp settings on the Heroku website. Under Config VARS, add a variable Disable_CollectStatic: 1.
