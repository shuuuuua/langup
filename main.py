# -*- coding: utf-8 -*-
import os

from flask import Flask, render_template, request
from google.cloud import storage

app = Flask(__name__)

@app.route("/")
def menu():
    return render_template('index.html')

@app.route("/shadowing_list")
def shadowing_list():

    shadowing_materials_bucket_name = 'langup-shadowing_stuff'
    storage_client = storage.Client()
    blobs = storage_client.list_blobs(shadowing_materials_bucket_name, prefix='voices/')
    mp3_list = [blob.name for blob in blobs if blob.name.endswith('.mp3')]
    
    return render_template('shadowing_list.html', mp3_list = mp3_list)

@app.route("/shadowing/<id>", methods=['GET'])
def shadowing():
    return render_template('shadowing.html')

@app.route("/flash_speaking")
def flash_speaking():
    categories = ['Business1-1', 'Business1-2', 'Business1-3']
    return render_template('flash_speaking.html', categories=categories)

@app.route("/flash_speaking_play/<string:category>/<int:marked>/<int:idx>")
def flash_speaking_play(category, marked=1, idx=0):
    flash_speaking_bucket_name = 'langup-flash-speaking'
    storage_client = storage.Client()
    bucket = storage_client.bucket(flash_speaking_bucket_name)
    blob_contents = bucket.blob(category + '.tsv').download_as_text()

    sentences = []
    for line in blob_contents.split('\n'):
        items = line.split('\t')
        if marked and items[3] is None:
            continue
        sentences.append((items[0], items[1]))
    if idx > len(sentences):
        return render_template('flash_speaking.html', categories=categories)
    else:
        return render_template('flash_speaking_play.html', sentence=sentences[idx], marked=marked, idx=idx)

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

if __name__ == "__main__":
    #app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
    app.run(debug=True)
