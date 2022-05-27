from bs4 import BeautifulSoup as bs
from splinter import Browser
import time
import requests
from webdriver_manager.chrome import ChromeDriverManager
from PIL import Image
def save_pic(vid_loc):
    img= Image.open(requests.get(vid_loc).content).convert('RGB')
    img_name =vid_loc.split(' ')[0]
    pic_loc =f'/data/{img_name}.jpg'
    img.save(pic_loc,'jpeg')
    return pic_loc


def scrape_vid_loc(url):

    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    call_return = {}

    browser.visit(url)
    time.sleep(1)

    page= browser.html

    soup = bs(page, 'html.parser')

    video_tags = soup.find_all('video')

    browser.quit()

    
    if len(video_tags) != 0:
        for video_tag in video_tags:
            video_url = video_tag['poster']
            return video_url
    else:
        return 404