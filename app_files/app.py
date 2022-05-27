
from re import I
from flask import Flask, render_template, redirect
import os, requests
import cam_scrape, weather_predictor, time
from apscheduler.schedulers.background import BackgroundScheduler
from pathlib import Path

fle = Path('data.py')
fle.touch(exist_ok=True)
f = open(fle)
app = Flask(__name__)


url ='https://www.skylinewebcams.com/en/webcam/mexico/nuevo-leon/monterrey/panorama-de-monterrey.html'

weather =['',0]
img = ''
def scrape():
    img_url = cam_scrape.scrape_vid_loc(url)
    global img 
    img = requests.get(img_url).content
    image = requests.get(img_url).content
    with open(f'templates/temp/image.jpg', 'wb+') as f:
        f.write(image)
    global weather 
    weather = weather_predictor.weather_prediction(f'templates/temp/image.jpg', accuracy= True)

scheduler = BackgroundScheduler()
job = scheduler.add_job(scrape, 'interval', minutes=15)
scheduler.start()




@app.route('/')
def index():
    global weather
    return render_template('index.html',image1 = '/temp_pic',weather1 = weather[0],accuracy1=weather[1])

@app.route('/temp_pic')
def picture():

    return img

@app.route('/reload')
def reload():
    scrape()
    global weather
    return render_template('index.html',image1 = '/temp_pic',weather1 = weather[0],accuracy1=weather[1])

if __name__ == "__main__":
    app.run(host= 'localhost',port =5000,debug=True)