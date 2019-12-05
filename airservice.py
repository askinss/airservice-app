from flask import Flask, request
import requests
from flask_jwt import JWT, jwt_required


# Credentials for authorised user to generate a token for authorised API call
USER_DATA = {
    "lunatech": "devops"
}
URL = "http://0.0.0.0:8080/"


app = Flask(__name__)
# Secret key for token
app.config['SECRET_KEY'] = 'luna-secret'

#Configure User to generate token
class User(object):
    '''
    User Class setup to handle JWT
    '''
    def __init__(self, id):
        self.id = id

    def __str__(self):
        return "User(id='%s')" % self.id


def verify(username, password):
    if not (username and password):
        return False
    if USER_DATA.get(username) == password:
        return User(id=100)


def identity(payload):
    user_id = payload['identity']
    return {"user_id": user_id}

#setup JsonWeb Token
jwt = JWT(app, verify, identity)


@app.route('/airports', methods=['GET'])
#Ensure no unauthorised access to URL
@jwt_required()
def airports():
    try:
        val = request.args['full']
        airports_info = requests.get("http://0.0.0.0:8082/airports?full={}".format(val), timeout=5).json()
        # print(airports_info)
    except (requests.RequestException, ValueError):
        return ValueError

    # return airports_info[0]["iso_country"]
    # return the airports in human readable format
    keys = [item['id'] for item in airports_info]
    return dict(zip(keys, airports_info))


@app.route('/airports/<id>',  methods=['GET'])
#Ensure no unauthorised access to URL
@jwt_required()
def airports_by_id(id):
    try:
        aport = requests.get("http://0.0.0.0:8082/airports"/{}.format(id), timeout=5)
        # print(airports_info)
    except (requests.RequestException, ValueError):
        return None

    return aport.content

@app.route('/search/<qry>',  methods=['GET'])
#Ensure no unauthorised access to URL
@jwt_required()
def search_by_qry(qry):
    try:
        aport = requests.get("http://0.0.0.0:8082/search"/{}.format(qry), timeout=5)
        # print(airports_info)
    except (requests.RequestException, ValueError):
        return None

    return aport.content



@app.route('/health/live',  methods=['GET'])
#Check if service is available
def healthlive():
    try:
        stat = requests.get("http://0.0.0.0:8082/health/live", timeout=5)
        

    except Exception as e:
        return e

    return {
        stat.status_code
    }

@app.route('/health/ready',  methods=['GET'])
# check the ready status of webservice
def healthready():
    try:
        stat = requests.get("http://0.0.0.0:8082/health/ready", timeout=5)
        
    except Exception as e:
        return e

    return {
        stat.status_code
    }


if __name__ == '__main__':
    app.run(debug=True)
