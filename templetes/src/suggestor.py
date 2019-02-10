#!flask/bin/python

from flask import Flask, render_template, request, redirect, Response
import random, json
from flask import make_response
app = Flask(__name__)

@app.route("/")
def output(msg):
    return render_template('web_page.html',msg)

@app.route('/receiver', methods=['POST'])
def worker():
    data = request.get_json()
    process_data(data)

def process_data(data):
    

if __name__ == "__main__":
    app.run(debug = True)