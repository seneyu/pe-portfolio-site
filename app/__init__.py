import os
from flask import Flask, render_template, request
from dotenv import load_dotenv
from jinja2 import Environment, PackageLoader, select_autoescape

env = Environment(
    loader=PackageLoader("app"),
    autoescape=select_autoescape()
)

load_dotenv()
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', title="MLH Fellow", url=os.getenv("URL"))

@app.route('/lucas/hobbies')
def hobbies():
    hobbies = [
        {
            "name": "Basketball",
            "description": "I love to play basketball and watch it.",
            "image_url": "/static/img/lucas-basketball.jpg"
        },
        {
            "name": "Hackathons",
            "description": "I love to hack and build things.",
            "image_url": "/static/img/lucas-hackathon.jpeg"
        },
    ]
    return env.get_template('hobbies.html').render(title="Hobbies", url=os.getenv("URL"), hobbies=hobbies, image_url="/static/img/lucas-picture.png")