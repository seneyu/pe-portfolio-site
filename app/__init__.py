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

@app.route('/lucas/education')
def lucas_education():
    education = [
        {
            "school": "University of Waterloo",
            "degree": "Software Engineering",
            "start_date": "Sept. 2024",
            "end_date": "Present"
        }
    ]

    return env.get_template('education.html').render(title="Education", url=os.getenv("URL"), education=education, image_url="/static/img/lucas-picture.png")

@app.route('/lucas')
def lucas():
    return render_template('lucas.html', title="Lucas", url=os.getenv("URL"))
