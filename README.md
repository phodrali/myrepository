## Introduction

This project provides endpoint to get the TODO of provided id.
We can see the list of all the todos from the below thirdparty api.
https://jsonplaceholder.typicode.com/todos

## Pre-requisites:
  - Linux server
  - Postgres DB installed on same server 
  - Need Database called test with user test and password test. DB test should have table called myDB with columns id, title, userid, completed
  - python3 with listed in python packages in requirement.txt
  
# Running project:
   `Server side:`
      Run the below command

	  python3 app.py
	  
   `Client side:`
      Run the below command
      
      curl http://127.0.0.1:5002/todo/12
	     or
	  curl -X GET http://127.0.0.1:5002/todo/12
	  
## Output:
   `Server side:`

```
postgres@239bbf1bc245:/usr/src/app/app$ python3 app.py
 * Serving Flask app 'app' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://127.0.0.1:5002/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 219-435-818
Getting todos from the DB for id 5
Connecting to db test
Disconnecting from db test
Could not find the todos for id 5 from DB
Getting todos for id 5 from thirdparty
https://jsonplaceholder.typicode.com/todos/5
Connecting to db test
INSERT INTO myDB (id,userid,title,completed) VALUES (5,1,'laboriosam mollitia et enim quasi adipisci quia provident illum',False)
INSERT 0 1
Disconnecting from db test
Successfully added record in DB
127.0.0.1 - - [27/Oct/2021 13:58:54] "GET /todo/5 HTTP/1.1" 200 -
Getting todos from the DB for id 5
Connecting to db test
Disconnecting from db test
127.0.0.1 - - [27/Oct/2021 13:59:23] "GET /todo/5 HTTP/1.1" 200 -
```

   `Client side:`

```   
postgres@239bbf1bc245:/$ curl http://127.0.0.1:5002/todo/1
{
  "content": {
    "completed": false,
    "id": 1,
    "title": "This is example",
    "userId": 3
  },
  "status": 200
}
```
```
postgres@239bbf1bc245:/$ curl http://127.0.0.1:5002/todo/12
{
  "content": {
    "completed": true,
    "id": 12,
    <!-- "title": "ipsa repellendus fugit nisi", -->
    "userId": 1
  },
  "status": 200
}
```
```
postgres@239bbf1bc245:/$ curl http://127.0.0.1:5002/todo/12
{
  "content": {
    "completed": true,
    "id": 12,
    "title": "ipsa repellendus fugit nisi",
    "userId": 1
  },
  "status": 200
}
```

# Design
The design of the project is available in the doc https://docs.google.com/document/d/1U8ryPMMG1Tu_1nnJXz-ccy6Srxu-E_bARHZ0RgFyA7g/edit?usp=sharing

