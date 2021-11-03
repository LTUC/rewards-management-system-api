# Expanded Endpoints Documentaton:

- ***/api/v#/courses/:id***  : This end point will prrvide you with a list of courses and all avaliable information about each of this courses.

    ***Request:***
    * GET: 

        **Responses:**
        1. *200 (OK)* : 
            *  data will be shaped as ***JSON List***:
            ```JSON
            [
            {
                "id": 1,
                "students": [
                                {
                                    "id": 27,
                                    "first_name": "example",
                                    "last_name": "example",
                                    "course": 1
                                },
                                {
                                    "id": 20,
                                    "first_name": "example",
                                    "last_name": "example",
                                    "course": 1
                                },
                                {
                                    "id": 14,
                                    "first_name": "example",
                                    "last_name": "example",
                                    "course": 1
                                },
                                {
                                    "id": 13,
                                    "first_name": "example",
                                    "last_name": "example",
                                    "course": 1
                                },
                                {
                                    "id": 7,
                                    "first_name": "example",
                                    "last_name": "example",
                                    "course": 1
                                },
                                {
                                    "id": 1,
                                    "first_name": "example",
                                    "last_name": "example",
                                    "course": 1
                                }
                            ],
                "code": "example-example-example",
                "instructor": "example example",
                "tas": {
                        "tas": [
                                    "example example",
                                    "example example",
                                    "example example",
                                    "example example",
            
                                ]
                        }
            },
            ]

            ```
    
    * POST:
        **Request:**
        1. *201 (OK)* : 
            *  data must be shaped as ***JSON object***:
            ```JSON
                {
                
       
                    "code": "example-example-example",
                    "instructor": "example example",
                    "tas": {
                        "tas": [
                                    "example example",
                                    "example example"
                                ]
                            }
               
                }
            ```
        **Response**
        *data will be shaped as ***JSON Object***
        ```JSON
             {
                
       
                    "code": "example-example-example",
                    "instructor": "example example",
                    "tas": {
                        "tas": [
                                    "example example",
                                    "example example"
                                ]
                            }
               
                }
        ```

    
- ***/api/v#/courses/id***  : This end point will prrvide you with information about a spacific course related to the id number.

    ***Request:***
    * GET: 

        **Responses:**
        1. *200 (OK)* : 
            *  data will be shaped as ***JSON Object***:
            ```JSON
                {
                
       
                    "code": "example-example-example",
                    "instructor": "example example",
                    "tas": {
                        "tas": [
                                    "example example",
                                    "example example"
                                ]
                        }
               
                }
            ```
    
    * PUT, PATCH and DELETE requests are be accepted for the end point with id.
        


- ***api/v#/students/:id***  : Which will retrun all points for cohort or specifc student

    ***Requests:***

    * GET: ***normall get request method***

        **Responses:**
        1. *200 (OK)* :
            *  data will be shaped as ***JSON list***:
            ```JSON
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



        * POST: 

        **Request:**
        1. *201 (OK)* :
            *  data must be shaped as ***JSON object***:
            ```JSON
                {
	
                "first_name": "example",
                "last_name": "example",
                "course_id": 1
                }
            ```
        **Response**
        ```JSON
            {
            "id": 31,
            "first_name": "example",
            "last_name": "example",
            "course": 1
            }
        ```

- ***/api/v#/students/id***  : This end point will prrvide you with information about a spacific student related to the id number.

    ***Request:***
    * GET: 

        **Responses:**
        1. *200 (OK)* : 
            *  data will be shaped as ***JSON Object***:
            ```JSON
               {
                "id": 31,
                "first_name": "Ahmad",
                "last_name": "Almohammad",
                "course": 1
                }
            ```
    
    * PUT, PATCH and DELETE requests are be accepted for the end point with id.
    ---------------------------------------------
    <br/>


- ***api/v#/rewards/:id***  : This end point will provide you with information about unclaimed rewards.

    ***Requests:***

    * GET: ***normall get request method***

        **Responses:**
        1. *200 (OK)* :
            *  data will be shaped as ***JSON list***:
            ```JSON
                [
                    {
                        "id": 1,
                        "owner":{
                            "id": 25,
                            "first_name": "example",
                            "last_name": "example",
                            "course": 6
                        },
                    "reward": "+1 mark on any submission",
                    "is_confirmed": false,
                    "created_at": "2021-10-29T19:39:35.670135Z"
                    },
                    {
                        "id": 2,
                        "owner": {
                            "id": 5,
                            "first_name": "example",
                            "last_name": "example",
                            "course": 5
                        },
                        "reward": "Resubmit attempt",
                        "is_confirmed": false,
                        "created_at": "2021-10-29T19:39:46.031323Z"
                    },
                    {
                        "id": 3,
                        "owner": {
                            "id": 7,
                            "first_name": "example",
                            "last_name": "example",
                            "course": 1
                        },
                        "reward": "Waive Late Assignment Penalty",
                        "is_confirmed": false,
                        "created_at": "2021-10-29T19:39:57.326885Z"
                    },
                    {
                        "id": 4,
                        "owner": {
                            "id": 13,
                            "first_name": "example",
                            "last_name": "example",
                            "course": 1
                        },
                        "reward": "Waive Late of class penalty",
                        "is_confirmed": false,
                        "created_at": "2021-10-29T19:40:11.292112Z"
                    },
                    {
                        "id": 5,
                        "owner": {
                            "id": 1,
                            "first_name": "example",
                            "last_name": "example",
                            "course": 1
                        },
                        "reward": "Waive Late of class penalty",
                        "is_confirmed": false,
                        "created_at": "2021-10-29T19:40:23.024015Z"
                    }
                ]
                ```


        * POST: 

        **Request:**
        1. *201 (OK)* :
            *  data must be shaped as ***JSON object***:
            ```JSON
            {
                "id": 1,
                "owner_id": 31,
                "reward": "+1 mark on any submission"
            }
            ```
        **Response**
        ```JSON
           {
                "id": 13,
                "owner": {
                    "id": 31,
                    "first_name": "example",
                    "last_name": "example",
                    "course": 1
                },
                "reward": "+1 mark on any submission",
                "is_confirmed": false,
                "created_at": "2021-10-30T16:22:55.033765Z"
            }
        ```
        * Where is_confirmed will take false as default value but you can provide it with other boolean types.



- ***/api/v#/rewards/id***  : This end point will prrvide you with information about a spacific claim related to the id number.

    ***Request:***
    * GET: 

        **Responses:**
        1. *200 (OK)* : 
            *  data will be shaped as ***JSON Object***:
            ```JSON
               {
                "id": 13,
                "owner": {
                    "id": 31,
                    "first_name": "example",
                    "last_name": "example",
                    "course": 1
                },
                "reward": "+1 mark on any submission",
                "is_confirmed": false,
                "created_at": "2021-10-30T16:22:55.033765Z"
                }
            ```
    
    * PUT, PATCH and DELETE requests are be accepted for the end point with id.
    ---------------------------------------------
    <br/>


## Filters: 

- You can filter the claims related to the owner id by adding it as params in the rewards end point.

    - Example:
    ***/api/v#/rewards/?id***

    **Responses:**
        1. *200 (OK)* :
            *  data will be shaped as ***JSON list***:

            ```JSON
                [
                    {
                        "id": 1,
                        "owner":{
                            "id": 25,
                            "first_name": "example",
                            "last_name": "example",
                            "course": 6
                        },
                    "reward": "+1 mark on any submission",
                    "is_confirmed": false,
                    "created_at": "2021-10-29T19:39:35.670135Z"
                    },
                    {
                        "id": 2,
                        "owner": {
                            "id": 25,
                            "first_name": "example",
                            "last_name": "example",
                            "course": 5
                        },
                        "reward": "Resubmit attempt",
                        "is_confirmed": false,
                        "created_at": "2021-10-29T19:39:46.031323Z"
                    }
                    
                ]
            ```

            
            
