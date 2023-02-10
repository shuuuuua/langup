# -*- coding: utf-8 -*-
import os
import random

from flask import Flask, render_template, redirect, url_for
import functions_framework
from google.cloud import storage

app = Flask(__name__)

random_seed = 0
flash_speaking_sentences = {}

@functions_framework.http
#@app.route("/")
def menu(request):
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
    categories = ['Business1-1', 'Business1-2', 'Business1-3-1', 'Advance1-1-1', 'Advance1-1-2']
    random_seed = int(random.random() * 100)
    return render_template('flash_speaking.html', categories=categories)

@app.route("/flash_speaking_category/<string:category>")
def flash_speaking_category(category):
    if category in flash_speaking_sentences.keys():
        pass
    else:
        flash_speaking_bucket_name = 'langup-flash-speaking'
        storage_client = storage.Client()
        bucket = storage_client.bucket(flash_speaking_bucket_name)
        blob_contents = bucket.blob(category + '.tsv').download_as_text()

        sentences = []
        for line in blob_contents.split('\r\n'):
            items = line.split('\t')
            sentences.append(tuple(items))
        flash_speaking_sentences[category] = sentences

    #print(sentences)
    return redirect(url_for('flash_speaking_play', category=category, marked=1, idx=1))
  

@app.route("/flash_speaking_play/<string:category>/<int:marked>/<int:idx>")
def flash_speaking_play(category, marked=1, idx=1):
    flash_speaking_bucket_name = 'langup-flash-speaking'
    storage_client = storage.Client()
    bucket = storage_client.bucket(flash_speaking_bucket_name)
    blob_contents = bucket.blob(category + '.tsv').download_as_text()

    if category not in flash_speaking_sentences.keys():
        return redirect(url_for('flash_speaking_category', category=category))

    sentences = [sentence for sentence in flash_speaking_sentences[category] if marked and sentence[4] == '1']
    #print(sentences)

    random.shuffle(sentences)
    total = len(sentences)
    if idx - 1 < total:
        return render_template('flash_speaking_play.html', sentence=sentences[idx-1], marked=marked, idx=idx, total=total)
    else:
        return redirect(url_for('flash_speaking'))

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
