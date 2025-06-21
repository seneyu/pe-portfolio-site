import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', title="MLH Fellow", url=os.getenv("URL"))

@app.route('/lucas/visited-places')
def lucas_visited_places():
    return render_template('visited-places.html', title="Visited Places", url=os.getenv("URL"), image_url="/static/img/lucas-picture.png", map_url="https://visitedplaces.com/embed/?map=world&projection=geoOrthographic&theme=dark-blue&water=1&graticule=0&names=1&duration=2000&placeduration=100&slider=0&autoplay=1&autozoom=none&autostep=1&home=CA&places=My%20Home~CA~1_0_0_96.5_-60.4*North%20America~US_PA_CU_DO~1.6_-100.6_44.4_100.6_-44.4*South%20America~BR~1.5_-65.9_-20.1_65.9_20.1*Europe~IT_FR_ES_PT~2.4_12.1_53.3_-12.1_-53.3")
