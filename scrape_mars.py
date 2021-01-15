from splinter import Browser
from bs4 import BeautifulSoup as bs
from webdriver_manager.chrome import ChromeDriverManager
from flask_Pymongo import pymongo
import time


def init_browser():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    return Browser("chrome", **executable_path, headless=False)


def scrape_info():
    browser = init_browser()

    url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
    browser.visit(url)

    time.sleep(1)

    html = browser.html
    soup = bs(html, 'lxml')

    titles = soup.find_all('div', class_='content_title'),
    paragraphs = soup.find_all('div', class_='article_teaser_body'),

    latest_headline = titles[1].text
    latest_summary = paragraphs[0].text

    ftr_img = 'https://www.jpl.nasa.gov/images/?search=&category=Mars'
    browser.visit(ftr_img)
    buttons = browser.find_by_tag('button')
    buttons[4].click()
    sourcesoup = bs(browser.html, 'lxml')
    img = sourcesoup.find_all(class_= 'text-subtitle-sm mb-2')[0].text.replace('\n', '').strip(),
    browser.links.find_by_partial_text(img).click() 
    browser.links.find_by_partial_text('Download JPG').click()
    imagesoup = bs(browser.html,'lxml')
    featured_img_url = imagesoup.find_all('img')[0]['src']
    featured_image = featured_img_url

    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars='
    browser.visit(url)

    hemisphere = []
    html = browser.html
    soup = bs(html, 'html.parser')
    sidebar = soup.find('div', class_='full-content')
    hemispheres = sidebar.find_all('div', class_='item')

    for item in hemispheres:
        hemisphere.append(item)

    titles = []
    images = []
    for y in hemispheres:
        image = y.find('a', class_='itemLink product-item')['href']
        images.append(image)

    urls = []
    relative_path = '.tif/full.jpg'

    for link in images:
        url = ['https://astrogeology.usgs.gov/' + link + relative_path]
        urls.append(url)

    vmpath = images[0]
    cerberuspath = images[1]
    schiaprellipath = images[2]
    smpath = images[3]

    Mars_data = {
        "headline": latest_headline,
        "lede": latest_summary,
        "Featured_Image": featured_image,
        "Valles_Marineris_Hemisphere": vmpath,
        "Cerberus Hemisphere": cerberuspath,
        "Schiaparelli Hemisphere": schiaprellipath,
        "Syrtis Major Hemisphere": smpath,
    }
    browser.quit()
    return Mars_data

    conn = 'mongodb://localhost:27017'
    client = pymongo.MongoClient(conn)
    db = client.MarsDB
    Mars = db.mission.find()
    db.Mars.insert_one(Mars_data)
