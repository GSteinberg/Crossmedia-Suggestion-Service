#!flask/bin/python

from flask import Flask, render_template, request, redirect, Response
import random, json
from flask import make_response
import csv

app = Flask(__name__)

@app.route("/")
def output(msg):
    return render_template('web_page.html',msg)

@app.route('/receiver', methods=['POST'])
def worker():
    data = request.get_json()
    print(data)
    process_data(data)

def process_data(data):
    with open ('art_database.csv') as a_csv:
        paints = csv.reader(a_csv, delimiter=',')


        song_sty = ''
        song_mood = ''

        for m in musics:
            if m[0] == data:
                song_sty = m[1]
                song_mood = m[2]

        sel_by_style = []
        sel_by_mood = []

        for p in paints:
            if p[1] == song_sty:
                sel_by_style.append(p)
            if p[2] == song_mood:
                sel_by_mood.append(p)

    imagenames = []
    for i in sel_by_style:
        for j in sel_by_mood:
            if i[0] == j[0]:
                imagenames.append(i[0])

    output(imagenames)


if __name__ == "__main__":
    app.run(debug = True)