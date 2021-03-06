# -*- coding: utf-8 -*-
import os

from flask import Flask, render_template, request
import urllib3

app = Flask(__name__)

@app.route("/")
#@app.route("/<id>", methods=['GET', 'POST'])
def show_menu():

    return render_template('index.html')

@app.route("/check", methods=['POST'])
def cehck():
    print(request.form.get('input'))
    input = request.form.get('input').replace(' ', '')
    name = request.form.get('alphabets').replace(' ', '')
    id = request.form.get('id')

    if input.lower() == name.lower():
        new_id = "{:03d}".format(random.randint(1, MONSTER_NO_MAX))
        return show(new_id)
    else:
        return show(id, mistake=True)

@app.route("/search")
def search():
    return render_template('search.html')

@app.route("/test")
def test():
    return render_template('test.html')

if __name__ == "__main__":
    #app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
    app.run(debug=True)