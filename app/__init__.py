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

@app.route('/lucas/work-experience')
def lucas_work_experience():
    work_experience = [
        {
            "company": "Shopify",
            "title": "Software Engineer Intern",
            "start_date": "May 2025",
            "end_date": "Present",
            "description": "Lending 💰"
        },
        {
            "company": "RBC",
            "title": "Innovation Developer",
            "start_date": "July 2024",
            "end_date": "Aug. 2024",
            "description": "Mortgages 🏠"
        },
        {
            "company": "NewArts Toronto",
            "title": "Website Manager and Developer",
            "start_date": "May 2023",
            "end_date": "Sept. 2023",
            "description": "Tutoring Platform 📚"
        },
        {
            "company": "GoalLine Solutions",
            "title": "Quality Assurance Intern",
            "start_date": "June 2023",
            "end_date": "Aug. 2023",
            "description": "Customer Analytics 📊"
        },
    ]
    return env.get_template('work-experience.html').render(title="Work Experience", url=os.getenv("URL"), work_experience=work_experience, image_url="/static/img/lucas-picture.png")
