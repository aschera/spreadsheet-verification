![Image 1](image1.jpg)
# Spreadsheet Verification

A web interface for uploading `.xlsx` files and verifying their content.

## Running the Server

To run the Django backend, follow these steps:

1. Open a terminal inside the project directory (`spreadsheet_verification`).
2. Type the following command:

```bash
python manage.py runserver
```

## Updates
To apply changes and updates, perform the following steps:

Open a terminal inside the project directory (spreadsheet_verification).
Run the following commands:

```bash
python manage.py makemigrations
python manage.py migrate
```

## File Storage
By default, Django uses SQLite for its database, suitable for development and testing purposes. The database file (db.sqlite3) will be created in the root directory of the project.

Database Configuration (settings.py)
```bash
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```
![Image 2](image2.jpg)

## Admin Panel
To access the admin panel, you need to create a superuser account:

Open a terminal inside the project directory (spreadsheet_verification).
Run the following command and follow the prompts:
```bash
python manage.py createsuperuser
```

Provide the requested information:

- Username
- Email
- Password

## Dependencies
List of external dependencies or libraries required to run the project goes here.

## Configuration
Details on any configuration settings or environment variables that need to be set up for the project.

## Testing
Instructions on how to run tests if implemented.

## Deployment
Deployment instructions or considerations, such as deploying to a cloud platform or setting up a production environment.

## Contributing
Guidelines for contributing to the project, including how to submit bug reports, feature requests, or pull requests.

## License
This project is open-source and available under the MIT License.
