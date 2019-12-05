AIRSERVICEAPP
=============

[![Build Status](https://travis-ci.org/askinss/airservice-app.svg?branch=master)](https://travis-ci.org/askinss/airservice-app)

### Start the Service.

		java -jar airports-assembly-1.0.3.jar
		git clone {{the project link you just copied}} Project
		cd Project
		docker build -t airservice:latest .
		docker run -p port:port airservice:latest

### Generate Tokens For Authorized Access:
 curl -H "Content-Type: application/json" -X POST -d '{"username":"lunatech","password":"devops"}' http://127.0.0.1:5000/auth
 "access_token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1NzU1NTUzMjIsImlhdCI6MTU3NTU1NTAyMiwibmJmIjoxNTc1NTU1MDIyLCJpZGVudGl0eSI6MTAwfQ.Gf5qcjb3WYTeudkuQJZOqxddAX-74-H8FQihT9WYZqo"
 }

 #### Use Token in Ger URL call
 curl -X GET http://127.0.0.1:500/airports -H "Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1NzU1NTUzMjIsImlhdCI6MTU3NTU1NTAyMiwibmJmIjoxNTc1NTU1MDIyLCJpZGVudGl0eSI6MTAwfQ.Gf5qcjb3WYTeudkuQJZOqxddAX-74-H8FQihT9WYZqo"
