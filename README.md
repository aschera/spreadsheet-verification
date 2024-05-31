# spreadsheet-verification
making a web interface to upload .xlsx files and verify their content. 

## Running the server
To run the Django backend, open a terminal inside the project (spreadsheet_verification) and type: python manage.py runserver

### Updates
When doing changed one has to migrate them.
Open a terminal inside the project (spreadsheet_verification) and type:
python manage.py makemigrations
python manage.py migrate

### File storage
By default, Django uses SQLite, which is suitable for development and testing purposes. Django will use SQLite by default. The database file will be named db.sqlite3 and located in the root directory of the project.

(see settings.py)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

### Admin panel
First, create a superuser account so you can log into the admin panel.
python manage.py createsuperuser
- username
- email
- password