from bs4 import BeautifulSoup as bs
from splinter import Browser
import time
import requests
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from PIL import Image


options = Options()
options.add_argument('headless')
options.add_argument('--disable-infobars')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--no-sandbox')
options.add_argument('--remote-debugging-port=9222')



def save_pic(vid_loc):
    img= Image.open(requests.get(vid_loc).content).convert('RGB')
    img_name =vid_loc.split(' ')[0]
    pic_loc =f'/data/{img_name}.jpg'
    img.save(pic_loc,'jpeg')
    return pic_loc



def scrape_vid_loc(url):

    browser = webdriver.Chrome(options=options)

    call_return = {}

    browser.get(url)
    time.sleep(1)

    

    soup = bs(browser.page_source, 'html.parser')

    video_tags = soup.find_all('video')

    browser.quit()

    
    if len(video_tags) != 0:
        for video_tag in video_tags:
            video_url = video_tag['poster']
            return video_url
    else:
        return 404