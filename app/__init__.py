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

@app.route('/lucas/visited-places')
def lucas_visited_places():
    return render_template('visited-places.html', title="Visited Places", url=os.getenv("URL"), image_url="/static/img/lucas-picture.png", map_url="https://visitedplaces.com/embed/?map=world&projection=geoOrthographic&theme=dark-blue&water=1&graticule=0&names=1&duration=2000&placeduration=100&slider=0&autoplay=1&autozoom=none&autostep=1&home=CA&places=My%20Home~CA~1_0_0_96.5_-60.4*North%20America~US_PA_CU_DO~1.6_-100.6_44.4_100.6_-44.4*South%20America~BR~1.5_-65.9_-20.1_65.9_20.1*Europe~IT_FR_ES_PT~2.4_12.1_53.3_-12.1_-53.3")

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

@app.route('/lucas/hobbies')
def lucas_hobbies():
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

@app.route('/stephany/about')
def stephany_about():
    description = "Hi! I am Stephany and I am interested in creating dynamic, interactive user experiences. Outside of coding, I like practicing yoga, doing film photography, and anything art related!"

    return render_template('about.html', 
                           title="About", url=os.getenv("URL"), 
                           image_url="/static/img/stephany-picture.JPG", 
                           description=description)