AIRSERVICEAPP
===============

[![Build Status](https://travis-ci.org/askinss/airservice-app.svg?branch=master)](https://travis-ci.org/askinss/airservice-app)

### Start the Service.

		java -Dhttp.port=8082 -jar airports-assembly-1.1.2.jar
		git clone {{the project link you just copied}} Project
		cd Project
		docker build -t airservice1.1:latest .
		docker run -p port:port airservice1.1:latest

