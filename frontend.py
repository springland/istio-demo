from flask import Flask
import requests
import os

app = Flask(__name__)

@app.route("/")
def index():    
    return "Front end "

@app.route("/backend")
def callbackend():
    url = os.getenv("backendurl")
    print("backendurl : " + url)
    response = requests.get(url)
    
    return "Front end calls backend, Receive response from " + response.text 


if __name__ == '__main__':
    print(' front end started')
    app.run('0.0.0.0' , 8080)
    
