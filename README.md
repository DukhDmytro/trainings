# Training schedule


Object of this task is to create a REST API to manage the training schedule.
User can register, login with JWT, get list of trainings and detils about single training.
Admin can add training to schedule, delete or update it using API or Django Admin panel.

## Admin panel and API documentation deployed on Heroku
Admin username: admin

Admin password: admin

[https://training-schedule.herokuapp.com/admin/](https://training-schedule.herokuapp.com/admin/)

[https://training-schedule.herokuapp.com/documentation/](https://training-schedule.herokuapp.com/documentation/)


## REST API endpoints
Api documentation, list of available resources and methods

`/documentation/`

POST method for registration of user. Admin can use GET, POST, PUT, DELETE

`users/`

Detail information about user

`users/username/`

Obtain JWT

`login/`

Refresh JWT

`login/refresh/`

Schedule of training

`schedule/`

Details about single training

`schedule/id/`

Admin panel

`admin/`

## Deploy on your local machine
1. Install requirements

`pip install -r requirements.txt`

2. Database settings

Rename example.env to .env and edit it
### Posgres
Set your db settings

`DB_NAME=database_name`
`DB_USER=user`
`DB_PASSWORD=password`

### SQLite
To use SQLite change DATABASES value in settings.py
`DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3'),
    }
}`

### Other settings
`SECRET_KEY=Your_secret_key`

### Migrations
`python manage.py makemigrations`

`python manage.py migrate`

### Start project

`python manage.py runserver`

### Running the tests
`python manage.py test`

### Superuser
`python manage.py createsuperuser`
