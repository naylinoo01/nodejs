#! usr/bin/python
# -*- coding: utf-8 -*-
import os
from os.path import join, dirname

from dotenv import load_dotenv
from flask import Flask, request, jsonify


dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
# OR, the same with increased verbosity:
load_dotenv(dotenv_path, verbose=True)



app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ["PORT"]))