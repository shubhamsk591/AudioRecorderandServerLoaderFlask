#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask
from flask import request
from flask import render_template
import os
import glob
import librosa
app = Flask(__name__)


@app.route("/", methods=['POST', 'GET'])

def index():
    if request.method == "POST":
        files = glob.glob('test_data/*')
        for f in files:
            os.remove(f)
        f = request.files['audio_data']
        with open('test_data/audio.wav', 'wb') as audio:
            f.save(audio)
        print('file uploaded successfully')
        data,sr=librosa.load(audio)
        print(sr)

        return render_template('index.html', request="POST")
    else:
        return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)