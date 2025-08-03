"""This is the main file for the application."""

import datetime
import os
from flask import Flask, render_template, request
from dotenv import load_dotenv
from jinja2 import Environment, PackageLoader, select_autoescape
from peewee import (
    CharField,
    DateTimeField,
    Model,
    MySQLDatabase,
    TextField,
    SqliteDatabase,
)
from playhouse.shortcuts import model_to_dict

env = Environment(loader=PackageLoader("app"), autoescape=select_autoescape())

load_dotenv()
app = Flask(__name__)

if os.getenv("TESTING") == "true":
    print("Running in test mode")
    mydb = SqliteDatabase("file=memory?mode=memory&cache=shared", uri=True)
else:
    mydb = MySQLDatabase(
        os.getenv("MYSQL_DATABASE"),
        user=os.getenv("MYSQL_USER"),
        password=os.getenv("MYSQL_PASSWORD"),
        host=os.getenv("MYSQL_HOST"),
        port=3306,
    )


class TimelinePost(Model):
    """A post on the timeline page."""

    name = CharField()
    email = CharField()
    content = TextField()
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        """Meta configuration for the TimelinePost model."""

        database = mydb


mydb.connect()
mydb.create_tables([TimelinePost])


@app.route("/")
def index():
    """The home page."""

    return render_template(
        "index.html",
        title="MLH Fellow Portfolios",
        url=os.getenv("URL"),
        names={"Lucas": "/lucas", "Stephany": "/stephany"},
    )


@app.route("/lucas/visited-places")
def lucas_visited_places():
    """The visited places page for Lucas."""

    return env.get_template("visited-places.html").render(
        title="Visited Places",
        url=os.getenv("URL"),
        image_url="/static/img/lucas-picture.png",
        map_url=(
            "https://visitedplaces.com/embed/?map=world&projection=geoOrthographic&"
            "theme=dark-blue&water=1&graticule=0&names=1&duration=2000&placeduration=100&"
            "slider=0&autoplay=1&autozoom=none&autostep=1&home=CA&places=My%20Home~CA"
            "~1_0_0_96.5_-60.4*North%20America~US_PA_CU_DO~1.6_-100.6_44.4_100.6_-44.4"
            "*South%20America~BR~1.5_-65.9_-20.1_65.9_20.1*Europe~IT_FR_ES_PT~"
            "2.4_12.1_53.3_-12.1_-53.3"
        ),
        name_url="/lucas",
        name="Lucas",
    )


@app.route("/lucas/education")
def lucas_education():
    """The education page for Lucas."""

    education = [
        {
            "school": "University of Waterloo",
            "degree": "Software Engineering",
            "start_date": "Sept. 2024",
            "end_date": "Present",
        },
        {
            "school": "Marc Garneau Collegiate Institute",
            "degree": "TOPS Program",
            "start_date": "Sept. 2020",
            "end_date": "June 2024",
        },
    ]

    return env.get_template("education.html").render(
        title="Education",
        url=os.getenv("URL"),
        education=education,
        image_url="/static/img/lucas-picture.png",
        name_url="/lucas",
        name="Lucas",
    )


@app.route("/lucas/work-experience")
def lucas_work_experience():
    """The work experience page for Lucas."""

    work_experience = [
        {
            "company": "Shopify",
            "title": "Software Engineer Intern",
            "start_date": "May 2025",
            "end_date": "Present",
            "description": "Lending 💰",
        },
        {
            "company": "RBC",
            "title": "Innovation Developer",
            "start_date": "July 2024",
            "end_date": "Aug. 2024",
            "description": "Mortgages 🏠",
        },
        {
            "company": "NewArts Toronto",
            "title": "Website Manager and Developer",
            "start_date": "May 2023",
            "end_date": "Sept. 2023",
            "description": "Online tutoring 📚",
        },
        {
            "company": "GoalLine Solutions",
            "title": "Quality Assurance Intern",
            "start_date": "June 2023",
            "end_date": "Aug. 2023",
            "description": "Customer Analytics 📊",
        },
    ]
    return env.get_template("work-experience.html").render(
        title="Work Experience",
        url=os.getenv("URL"),
        work_experience=work_experience,
        image_url="/static/img/lucas-picture.png",
        name_url="/lucas",
        name="Lucas",
    )


@app.route("/lucas/hobbies")
def lucas_hobbies():
    """The hobbies page for Lucas."""

    hobbies = [
        {
            "name": "Basketball",
            "description": "I love to play basketball and watch it.",
            "image_url": "/static/img/lucas-basketball.jpg",
        },
        {
            "name": "Hackathons",
            "description": "I love to hack and build things.",
            "image_url": "/static/img/lucas-hackathon.jpeg",
        },
    ]
    return env.get_template("hobbies.html").render(
        title="Hobbies",
        name="Lucas",
        url=os.getenv("URL"),
        hobbies=hobbies,
        image_url="/static/img/lucas-picture.png",
        name_url="/lucas",
    )


@app.route("/lucas/about")
def lucas_about():
    """The about page for Lucas."""

    description = (
        "Hey! My name is Lucas and I'm majoring in Software Engineering at Waterloo. "
        "Outside of coding, I love to play/watch basketball and other sports!"
    )

    return render_template(
        "about.html",
        title="About",
        url=os.getenv("URL"),
        image_url="/static/img/lucas-picture.png",
        description=description,
        name_url="/lucas",
        name="Lucas",
    )


@app.route("/lucas/timeline")
def lucas_timeline():
    """The timeline page for Lucas."""

    posts = TimelinePost.select().order_by(TimelinePost.created_at.desc())

    return env.get_template("timeline.html").render(
        title="Timeline",
        url=os.getenv("URL"),
        image_url="/static/img/lucas-picture.png",
        name_url="/lucas",
        name="Lucas",
        posts=posts,
    )


@app.route("/lucas")
def lucas():
    """The home page for Lucas."""

    return env.get_template("lucas.html").render(
        title="Lucas",
        url=os.getenv("URL"),
        image_url="/static/img/lucas-picture.png",
        name_url="/lucas",
        name="Lucas",
    )


@app.route("/stephany/visited-places")
def stephany_visited_places():
    """The visited places page for Stephany."""

    return env.get_template("visited-places.html").render(
        title="Visited Places",
        url=os.getenv("URL"),
        image_url="/static/img/stephany-picture.JPG",
        map_url=(
            "https://visitedplaces.com/view/?map=world&projection=geoEqualEarth&"
            "theme=dark-blue&water=1&graticule=0&names=1&duration=2000&placeduration=100&"
            "slider=0&autoplay=0&autozoom=none&autostep=1&home=HK&places=~HK.cc9f40*Asia~"
            "CN_JP_TH~1.9_75_30.8_-84.7_0*North%20America~US_CA~2.2_-97_41_85.3_0*Europe~"
            "GB_IT_FR_CH~3.1_21.3_47.1_-19_0"
        ),
        name_url="/stephany",
        name="Stephany",
    )


@app.route("/stephany/education")
def stephany_education():
    """The education page for Stephany."""

    education = [
        {
            "school": "University of California, Davis",
            "degree": "Bachelor of Science",
        }
    ]

    return env.get_template("education.html").render(
        title="Education",
        url=os.getenv("URL"),
        education=education,
        image_url="/static/img/stephany-picture.JPG",
        name_url="/stephany",
        name="Stephany",
    )


@app.route("/stephany/hobbies")
def stephany_hobbies():
    """The hobbies page for Stephany."""

    hobbies = [
        {
            "name": "Performing Arts",
            "description": (
                "I love watching and exploring performing arts. "
                "I joined a beginner physical theater performance."
            ),
            "image_url": "/static/img/steph-hobby1.JPG",
        },
        {
            "name": "Film Photography",
            "description": (
                "I like taking photos with film cameras. "
                "Here is me taking a selfie with my Olympus XA."
            ),
            "image_url": "/static/img/steph-hobby2.PNG",
        },
    ]
    return env.get_template("hobbies.html").render(
        title="Hobbies",
        url=os.getenv("URL"),
        hobbies=hobbies,
        image_url="/static/img/stephany-picture.JPG",
        name_url="/stephany",
        name="Stephany",
    )


@app.route("/stephany/work-experience")
def stephany_work_experience():
    """The work experience page for Stephany."""

    work_experience = [
        {
            "company": "Alki",
            "title": "Software Engineer",
            "start_date": "Nov 2024",
            "end_date": "Present",
            "description": "SaaS",
        },
        {
            "company": "OSLabs",
            "title": "Software Engineer",
            "start_date": "Mar 2024",
            "end_date": "Dec 2024",
            "description": "Open Source",
        },
    ]
    return env.get_template("work-experience.html").render(
        title="Work Experience",
        url=os.getenv("URL"),
        work_experience=work_experience,
        image_url="/static/img/stephany-picture.JPG",
        name_url="/stephany",
        name="Stephany",
    )


@app.route("/stephany/about")
def stephany_about():
    """The about page for Stephany."""

    description = (
        "Hi! I am Stephany and I am interested in creating dynamic, interactive user "
        "experiences. Outside of coding, I like practicing yoga, doing film photography, "
        "and anything art related!"
    )

    return render_template(
        "about.html",
        title="About",
        url=os.getenv("URL"),
        image_url="/static/img/stephany-picture.JPG",
        description=description,
        name_url="/stephany",
        name="Stephany",
    )


@app.route("/stephany")
def stephany():
    """The home page for Stephany."""

    return env.get_template("layout.html").render(
        title="Home",
        url=os.getenv("URL"),
        image_url="static/img/stephany-picture.jpg",
        name_url="/stephany",
        name="Stephany",
    )


@app.route("/api/timeline_post", methods=["POST"])
def post_timeline_post():
    """Post a timeline post."""

    name = request.form.get("name", "").strip()
    email = request.form.get("email", "").strip()
    content = request.form.get("content", "").strip()

    if not name:
        return "Invalid name", 400
    if not content:
        return "Invalid content", 400
    if "@" not in email or not email:
        return "Invalid email", 400

    timeline_post = TimelinePost.create(name=name, email=email, content=content)

    return model_to_dict(timeline_post)


@app.route("/api/timeline_post")
def get_timeline_post():
    """Get a timeline post."""

    return {
        "timeline_posts": [
            model_to_dict(p)
            for p in TimelinePost.select().order_by(TimelinePost.created_at.desc())
        ]
    }


@app.route("/api/timeline_post", methods=["DELETE"])
def delete_timeline_post():
    """Delete a timeline post."""

    post_id = request.form["id"]
    deleted = TimelinePost.delete_by_id(post_id)
    if deleted:
        return {"deleted": post_id}
    else:
        return {"error": "Not found"}, 404
