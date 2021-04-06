# A Django App
*Description will go here...*
## Installation
### Clone the repo

### Environment
( *Note: As the Django version used by this app is `3.1.7`, the compatible python versions are `3.6, 3.7, 3.8, 3.9`. So make sure that you have compatible version of python installed in your system or at least in your virtual environment.* )\
Go to app root directory `/django-app` then create a python virtual environment
```
# considering your system has compatible python version installed
.../django-app$ python3 -m venv app-env
```
Then activate the virtual environment.
```
.../django-app$ source app-env/bin/activate
```
You should see the name of virtual environment in the terminal like this:
```
(app-env) .../django-app$ 
```
You can setup the virtual environment with other packages as well, like `pyenv`, `virtualenv` etc.

Check the version of pip
```
(app-env) .../django-app$ pip -V
```
If not latest, upgrade the pip as well
```
(app-env) .../django-app$ pip install --upgrade pip
```

For the environment variables, copy the `env.sample` file to `.env` and change the variables in `.env` file according to your setup.
```
(app-env) .../django-app$ cp env.sample .env
```

### Package installation
All python packages/libraries required for this app are listed in the `requirements.txt`. To install them enter this command:
```
(app-env) .../django-app$ pip install -r requirements.txt
```

### Database
This application uses PostgreSQL (v13) as database. You can install/download it from [here](https://www.postgresql.org/download/) and follow the instructions for your system.

After the download is complete create a user and provide the credentials in `.env` file.

## Migration
To run the migration
```
(app-env) .../django-app$ cd jubelash
(app-env) .../django-app/jubelash$ python3 manage.py migrate
```

## Admin Creation
Django provides feature to manage users and groups in the same app, which requires user login. For that you need to create an admin and manage other users after logging in as admin.

So to create an admin you can do
```
(app-env) .../django-app/jubelash$ python3 manage.py createsuperuser
```
and answer the prompts.

You can login using the credentials you entered from page '`/{ADMIN_PAGE_PATH}`' (defined in the `.env` file).

## Run
To run the app, enter this command:
```
(app-env) .../django-app/jubelash$ python3 manage.py runserver
```
