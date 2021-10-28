# Expanded Endpoints Documentaton:

<br/>
<br/>

--------------------------------------

- ***data/***  : witch will retrun all cohort data (students, TAs, instructors)

    ***Request:***
    * GET: ***normall get request method only allowed***

        **Responses:**
        1. *200 (OK)* : 
            *  response data will be shaped as ***Object***:
            ```
            {
                'Cohort Name (py-d6)':{
                    "Instructor":"Instructor Name",
                    "TAs":['TAs Names'],
                    "Students":['All Students Names']
                }
            }
            ```
            > response status always will be 200

<br/>
<br/>

--------------------------------------

- ***points/***  : witch will retrun all points for cohort or specifc student

    ***Requests:***

    * GET: ***normall get request method***

        **Responses:**
        1. *200 (OK)* :
            *  response data will be shaped as ***Array***:
            ```
            [
                {
                    "id": 1,
                    "owner": "Student Name",
                    "reward": "Waive Late of class penalty",
                    "is_confirmed": false,
                    "created_at": "2021-10-26T22:38:55.586653Z",
                    "updated_at": "2021-10-28T03:44:00.200307Z"
                },
                {
                    "id": 2,
                    "owner": "Student Name",
                    "reward": "+1 mark on any submission",
                    "is_confirmed": false,
                    "created_at": "2021-10-26T22:39:54.973384Z",
                    "updated_at": "2021-10-28T03:44:00.200307Z"
                },
                {
                    "id": 3,
                    "owner": "Student Name",
                    "reward": "+1 mark on any submission",
                    "is_confirmed": false,
                    "created_at": "2021-10-26T23:35:13.935744Z",
                    "updated_at": "2021-10-28T03:44:00.200307Z"
                }
            ]
            ```

    ---------------------------------------------
    <br/>

    * GET: ***costmized get request method*** with adding `"by_student":"Student Name"` to the request body, points will returend only that Student Own

        **Responses:**
        1. *200 (OK)* : in case student exist and have points or student not exist
            *  response data will be shaped as ***Array***:
            ```
            [
                {
                    "id": 4,
                    "owner": "Passed Student Name",
                    "reward": "Waive Late of class penalty",
                    "is_confirmed": false,
                    "created_at": "2021-10-26T22:38:55.586653Z",
                    "updated_at": "2021-10-28T03:44:00.200307Z"
                },
                {
                    "id": 9,
                    "owner": "Passed Student Name",
                    "reward": "+1 mark on any submission",
                    "is_confirmed": false,
                    "created_at": "2021-10-26T22:39:54.973384Z",
                    "updated_at": "2021-10-28T03:44:00.200307Z"
                }
            ]
            ```
            > even if user own **1 point** data will always returned as an ***Array***

        <br/>

        2. *400 (BAD REQUEST)* : in case student dose'nt have any points
            *  response data will be shaped as ***Object***:
            ```
            {
                "error": "no points for this student"
            }
            ```
            ---------------------------------------------
    <br/>

    * GET: ***costmized get request method*** with adding `"by_confirmation":"Boolen Field"` to the request body, points will returend by is_confirmed field status

        **Responses:**
        1. *200 (OK)* : in case by_confirmation is real Boolean Value (true)
            *  response data will be shaped as ***Array***:
            ```
            [
                {
                    "id": 4,
                    "owner": "Passed Student Name",
                    "reward": "Waive Late of class penalty",
                    "is_confirmed": true,
                    "created_at": "2021-10-26T22:38:55.586653Z",
                    "updated_at": "2021-10-28T03:44:00.200307Z"
                },
                {
                    "id": 9,
                    "owner": "Passed Student Name",
                    "reward": "+1 mark on any submission",
                    "is_confirmed": true,
                    "created_at": "2021-10-26T22:39:54.973384Z",
                    "updated_at": "2021-10-28T03:44:00.200307Z"
                }
            ]
            ```
            > even if confirmed points was **1 point** data will always returned as an ***Array***

        <br/>

        2. *400 (BAD REQUEST)* : in case by_confirmation is **not** Boolean Value
            *  response data will be shaped as ***Object***:
            ```
            {
                "error": "by_confirmation field should be only Boolean"
            }
            ```
    ---------------------------------------------
    <br/>

    * POST: ***with 2 requierd vlaues in the body*** and it will create new point in the model for the passed owner(student)
        
        ```
        {
            "owner": "student name that will be given the point",
            "reward": "witch is choice field accepts only specifc values"
        }
        ```
        
        **^acceptable values in reward field:**
        1. Waive Late Assignment Penalty
        2. Waive Late of class penalty
        3. +1 mark on any submission
        4. Resubmit attempt

        <br/>

        **Responses:**
        1. *201 (CREATED)* : in case all data are valid and no missing data
            *  response data will be shaped as ***Object***:
            ```
            {
                "id": 10,
                "owner": "Passed Owner Name",
                "reward": "Waive Late Assignment Penalty",
                "is_confirmed": false,
                "created_at": "2021-10-26T22:38:55.586653Z",
                "updated_at": "2021-10-28T03:44:00.200307Z"
            }
            ```
            <br/>

        2. *400 (BAD REQUEST)* : in case missing any field
            *  response data will be shaped as ***Object***:
            ```
            {
                "Missing Field Name": [
                    "This field is required."
                ]
            }
            ```
<br/>
<br/>

--------------------------------------

- ***done-claim/< int:id >***  : witch will update only is_confirmed status for the passed point id 

    ***Requests:***

    * PUT: ***with 1 requierd vlaue in the body & requierd Param*** and it will update is_confirmed status for the passed point id 

        ```
        {
            "is_confirmed": Boolean Value
        }
        ```
        > any extra fields in the request body will be **ignored**
        
        <br/>

        **Responses:**
        1. *200 (OK)* : in case ***param:id=1 and body:is_confirmed=true***
            *  response data will be shaped as ***Object***:
            ```
            {
                "id": 1,
                "owner": "Student Name",
                "reward": "Waive Late of class penalty",
                "is_confirmed": true,
                "created_at": "2021-10-26T22:38:55.586653Z",
                "updated_at": "2021-10-28T03:44:00.200307Z"
            }
            ```
        
        <br/>

        2. *400 (BAD REQUEST)* : in case **no is_confirmed in the request**!
            *  response data will be shaped as ***Object***:
            ```
            {
                "error": "please send is_confirmed value only!"
            }
            ```
        
        <br/>

        3. *400 (BAD REQUEST)* : in case ***param id not exist***!
            *  response data will be shaped as ***Object***:
            ```
            {
                "error": "Point is not exist!!"
            }
            ```