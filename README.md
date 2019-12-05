AIRSERVICEAPP
=============

[![Build Status](https://travis-ci.org/askinss/airservice-app.svg?branch=master)](https://travis-ci.org/askinss/airservice-app)

### Start the Service.

		java -jar airports-assembly-1.0.3.jar
		git clone {{the project link you just copied}} Project
		cd Project
		docker build -t airservice:latest .
		docker run -p port:port airservice:latest
