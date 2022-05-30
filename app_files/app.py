
from flask import Flask, render_template, redirect, url_for
import os, requests
import cam_scrape, weather_predictor, time
from apscheduler.schedulers.background import BackgroundScheduler
from pathlib import Path
from PIL import Image


app = Flask(__name__)


urls = ['https://www.skylinewebcams.com/en/webcam/mexico/nuevo-leon/monterrey/panorama-de-monterrey.html','https://www.skylinewebcams.com/en/webcam/thailand/central-thailand/bangkok/bangkok-crossroads.html','https://www.skylinewebcams.com/en/webcam/iceland/austurland/hofn/jokulsarlon.html']
names = ['Monterrey_Mexico','Bangkok_thailand','Jokulsarlon_Iceland']
city_dropdown = ''

for city in names:
    city_formatted = city.replace("_",', ')
    city_dropdown = city_dropdown + f'''<a class="dropdown-item" href="../{city}">{city_formatted}</a>'''


weather ={'default':['',0]}
img = {'cloudy1':''}
def scrape():
    global urls
    global img 
    global weather 
    img = {'default':''}
    weather = {'default':['',0]}
    global names
    for url,name in zip(urls,names):

        img_url = cam_scrape.scrape_vid_loc(url)
        img[name] = requests.get(img_url).content
        image = requests.get(img_url).content
        with open(f'appdata/temp/{name}.jpg', 'wb+') as f:
            f.write(image)
        weather[name] = weather_predictor.weather_prediction(f'appdata/temp/{name}.jpg', accuracy= True)




scheduler = BackgroundScheduler()


@app.before_first_request
def activate_job():
    scrape()
    scheduler.add_job(scrape, 'interval', minutes=15)
    scheduler.start()

@app.route('/')
def index():
    img= url_for('static',filename='images/cloudy1.jpg')
    return render_template('index.html',citylist=city_dropdown, image=img)

@app.route('/<location>')
def place(location):
    global weather
    global city_dropdown
    location_formatted = location.replace("_",', ')
    return render_template('city.html',city =location_formatted,image1 = f'/pics/{location}',weather = weather[location][0],accuracy=round(weather[location][1]*100,2),
        citylist=city_dropdown)



@app.route('/pics/<location>')
def picture(location):

    return img[location]

# @app.route('/pics/testpicture')
# def testpic():
#     return ('<img src = "/static/images/cloudy1.jpg" />')

if __name__ == "__main__":
    app.run(host= 'localhost',port =5000,debug=True)