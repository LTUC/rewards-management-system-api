# Rewards Management System API (RMS_API)


### Project Description:

Simple API crud builded by Django Technology & Rest Framework

mainly RMS_API builded to serve the main project [RMS](https://github.com/LTUC/rewards-management-system) 

<br/>

-----------------------------------

### Requirements:

- poetry_dev-tool
- python = "^3.9"
- Django = "^3.2.8"
- djangorestframework = "^3.12.4"

<br/>

-----------------------------------

### Getting Started:

1. using your terminal start with `poetry install` to install the main dependencies for the project

2. after installing done you can start by sourcing project virtual environment by using `poetry shell`

3. your virtual environment are applied now its time to start some normal prosegures by `python mange.py makemigrations` witch is simply will collect what models going to be added as **tables** in the DB (data base)

4. migrating is th most important setp in starting any *django app* mainly it will convert your models to a real DB Tables so it will be ready to get the new records in the right place
migrating done ususaly by using `python mange.py migrate`

5. well it wasn't long steps! :) now you are ready to launch up and start your app server by runing: `python mange.py runserver` you will find that your terminal started the server and provided you with link to access your project [https://(locallhost):(port)]()

<br/>

-----------------------------------

### Endpoint Documentaton:

RMS_API using many https routs that will provide you with data and main endPoints are:

- ***admin/***  : witch will be responsible about guide you directly to the **django admin panel**

- ***data/***  : special route used to return to the user important json data about the names of cohorts and the instructional team that particpat in

- ***points/*** : witch accept 2 mthods:
    - GET: witch will retrun the points for each student with al point details 
    
    ^it may pass **"by_student"** with value of the student name and it will retrun only the points are related to this student in this case

    ^it may pass **"by_confirmation"** with Boolean value and it will retrun only the points are related to this value in is_confiermd field


    - POST: witch will create new point for the passed user so it requierd some data in the body request

- ***done-claim/< int:id >*** : witch accept only 1 method:
    - PUT: witch requierd an point id to be passed in the param and confirmation status for the point in the body

> read more details about [RMS Endpoints](./Endpoints_Documentaton.md)

<br/>

-----------------------------------

### Contributing:


<br/>

-----------------------------------

### Running Tests:

RMS_API contain some specifc local tests to test the main fetures implemntaion :

1. test_user_can_get_cohort_students
2. test_user_can_create_point
3. test_user_can_get_points
4. test_user_can_confirm_point

<br/>

-----------------------------------

### Self Hosting:



<br/>

-----------------------------------

# TODO
## Complete the following tasks in this README
- [x] Project Description
- [x] Requirements
- [x] Getting Started
- [x] Endpoint Documentaton
- [ ] Contributing
- [x] Running Tests
- [ ] Self Hosting

Contributors:
Author - https://github.com/3madov-77