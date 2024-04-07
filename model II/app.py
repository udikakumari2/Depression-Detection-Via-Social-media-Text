from flask import Flask, render_template, request
from flask_ngrok import run_with_ngrok
import streamlit as st
import pickle
from keras.preprocessing.sequence import pad_sequences

import numpy as np
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
# Load the tokenizer from the pickle file
with open('tokenizer.pkl', 'rb') as f:
    tokenizer = pickle.load(f)
import tensorflow as tf
from keras.models import load_model
import plotly.express as px
import pandas as pd
token_form = pickle.load(open('tokenizer.pkl', 'rb'))
model = load_model("model.h5")

template_folder = "F:\dd"  # Path to your templates folder
static_folder = "F:\dd\static"  # Path to your static folder containing CSS files

app = Flask(__name__, template_folder=template_folder, static_folder=static_folder)
run_with_ngrok(app)  # Integrate Ngrok with Flask

@app.route('/')
@app.route('/home',methods=[ 'POST'])
def home():
    text=request.form('text')
    pred=model.predict(text)
    print(pred)
    return render_template('home.html',pred=pred)

@app.route('/page', methods=['GET', 'POST'])
def page():
##    name=request.form('name')
##    email=request.form('email')

      
##    message=request.form('message')
      
##    if request.method == 'POST':
##        name = request.form.get('name')
##    else:
##        name = None
      ##name=input("enter name")
      return render_template('page.html', name=name)
      
    

@app.route('/score/<int:score>')
def score(score):
    return render_template('page1.html', score_value=score)

if __name__ == '__main__':
    app.run()
