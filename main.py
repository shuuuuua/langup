# -*- coding: utf-8 -*-
import os
import random

from flask import Flask, render_template, redirect, url_for
import functions_framework
from google.cloud import storage

app = Flask(__name__)

#random_seed = 0
flash_speaking_sentences = {}

#@functions_framework.http
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
    categories = ['Business1-1', 'Business1-2', 'Business1-3-1', 'Advance1-1-1', 'Advance1-1-2', 'Advance1-1-3',
                  'Advance1-2-1', 'Advance1-2-2', 'Advance1-3-1', 'Advance1-3-2', 
                  'BuildingVocabulary-01', 'BuildingVocabulary-02', 'BuildingVocabulary-03']
    return render_template('flash_speaking.html', categories=categories)

@app.route("/flash_speaking_category/<string:category>")
def flash_speaking_category(category):
    global flash_speaking_sentences
    if category not in flash_speaking_sentences.keys():
        flash_speaking_bucket_name = 'langup-flash-speaking'
        storage_client = storage.Client()
        bucket = storage_client.bucket(flash_speaking_bucket_name)
        blob_contents = bucket.blob(category + '.tsv').download_as_text()

        sentences = []
        for line in blob_contents.split('\r\n'):
            items = line.split('\t')
            sentences.append(tuple(items))
        random_seed = int(random.random() * 100)
        flash_speaking_sentences[category] = (random_seed, sentences)

    #global random_seed
    #random_seed = int(random.random() * 100)

    return redirect(url_for('flash_speaking_play', category=category, marked=1, idx=1))
  

@app.route("/flash_speaking_play/<string:category>/<int:marked>/<int:idx>")
def flash_speaking_play(category, marked=1, idx=1):
    #flash_speaking_bucket_name = 'langup-flash-speaking'
    #storage_client = storage.Client()
    #bucket = storage_client.bucket(flash_speaking_bucket_name)
    #blob_contents = bucket.blob(category + '.tsv').download_as_text()

    if category not in flash_speaking_sentences.keys():
        return redirect(url_for('flash_speaking_category', category=category))

    sentences = [sentence for sentence in flash_speaking_sentences[category][1] if marked and sentence[4] == '1']

    random.seed(flash_speaking_sentences[category][0])
    random.shuffle(sentences)
    total = min((len(sentences), 60))
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
    app.run(debug=False)
