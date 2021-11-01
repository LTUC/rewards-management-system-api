# Rewards Management System API (RMS_API)


### Project Description:

Simple API crud builded by Django Technology & Rest Framework

Mainly RMS_API builded to serve the main project [RMS](https://github.com/LTUC/rewards-management-system)

<br/>

-----------------------------------

### Requirements:

- python = 3.9
- Django = 3.2.8
- Django = 3.2.8
- djangorestframework = 3.12.4
- django-cors-headers = 3.10.0
- django-filter = 21.1
- django-debug-toolbar = 3.2.2
- gunicorn = 20.1.0
- whitenoise = 5.3.0
- psycopg2-binary = 2.9.1
- django-environ = 0.8.1

<br/>

-----------------------------------

### Getting Started locally:

1. You may have Docker and it should be setuped proparly.

2. In your terminal run the following command to build and start the services:

```
➜  rewards-management-system-api git:(branch) ✗ docker-compose up --build
```
3. All migrations file are in the repo but if you did some changes on the models so you ought to run this command:

```
➜  rewards-management-system-api git:(branch) ✗ docker-compose run web python manage.py makemigrations `app name that had been changes`
```
4. To migrate you need this command:
```
➜  rewards-management-system-api git:(branch) ✗ docker-compose run web python manage.py migrate
```

<br/>

-----------------------------------

### Endpoint Documentaton:

RMS_API using many https routs that will provide you with data and main endPoints are:

- ***admin/***  : This end point will be responsible about guide you directly to the **django admin panel**

- ***/api/v#/courses/***  : This end point will prrvide you with a list of courses and all avaliable information about each of this courses.

- ***api/v#/students/*** : This end point for all students names in our system.

- ***api/v#/rewards/*** : This end point will provide you with information about unclaimed rewards. 

- ***done-claim/< int:id >*** : witch accept only 1 method:
    - PUT: witch requierd an point id to be passed in the param and confirmation status for the point in the body

> read more details about [RMS Endpoints](./Endpoints_Documentaton.md)

<br/>
