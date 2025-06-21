import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', title="MLH Fellow", url=os.getenv("URL"))

@app.route('/lucas/about')
def lucas_about():
    description = "Hey! My name is Lucas and I'm majoring in Software Engineering at Waterloo. Outside of coding, I love to play/watch basketball and other sports!"

    return render_template('about.html',
                           title="About",
                           url=os.getenv("URL"),
                           image_url="img/lucas-picture.png",
                           description=description)

@app.route('/lucas')
def lucas():
    return render_template('lucas.html', title="Lucas", url=os.getenv("URL"))

