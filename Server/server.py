from flask import Flask, request
import json
from datetime import datetime
import os
app = Flask(__name__)

@app.route('/', methods = ['POST'])
def main():
    if(request.method == "POST"):
        data = request.json
        fileName = os.path.join("dataJSON", request.remote_addr + " " + datetime.now().strftime("%d-%m-%Y %H-%M-%S") + ".json")
        with open(fileName, "w") as json_file:
            json_file.write(json.dumps(data, indent=4))
    return "ok"