from flask import Flask
import requests


app = Flask(__name__)

@app.route("/")
def index():    
    url = "http://backend/"
    #url = "http://192.168.49.2:31766"
    
    return "Front end "

@app.route("/backend")
def callbackend():
    url = "http://backend:8080/"
    response = requests.get(url)
    
    return "Front end calls backend, Receive response from " + response.text 


if __name__ == '__main__':
    print(' front end started')
    app.run('0.0.0.0' , 8080)
    
