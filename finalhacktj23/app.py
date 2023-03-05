from flask import Flask, render_template, request, url_for, flash, redirect

app = Flask(__name__)
app.config['SECRET_KEY'] = 'AAAA'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/questions')
def questions():

    return render_template('questions.html')

@app.route('/snellentest')
def snellentest():
    data = {"size_mm" :20,"image" : 'E.png'}
    return render_template('snellentest.html',data = data)
