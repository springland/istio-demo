import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():    
    version = os.getenv("version")
    return "Backend  " + str(version) + "\n"


if __name__ == '__main__':
    print(' back end started')
    app.run('0.0.0.0' , 8080)
    
        