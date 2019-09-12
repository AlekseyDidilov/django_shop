# django_shop

## Deploy application

There are two ways to deploy the application.

#### Docker

This type of launch allows to create a docker container with
application on your PC.

To be able to use this type of run, you need to have
[Docker](https://www.docker.com/) engine release 18.06.1-ce

A simple way to check Docker:
```bash
docker --version
```
First of all, you need to run:
```bash
docker-compose up -d
```
The application will be available on localhost

If you want to shutdown docker you must run:
```bash
docker-compose down
```

#### Python

This type of launch running app by Python on your PC.

To be able to use this type of run, you need to have
[Python](https://www.python.org/) engine release 3.6.5 and
[PostgreSQL](https://www.postgresql.org/) engine release 11.5


A simple way to check Python:
```bash
python --version
``` 

or 

A simple way to check Python:
```bash
python3 --version
``` 

You must install correct versions of libraries:
```bash
pip install -r requirements.txt
``` 

Than you can run app:
```bash
python manage.py runserver
```
The application will be available on localhost:8000

Note that using this method you need to configure access to the 
database in the file store/settings.py

