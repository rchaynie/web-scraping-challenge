import pandas as pd
import requests
from bs4 import BeautifulSoup
import time
from splinter import Browser
import jsonify
import pymongo


CONN = "mongodb+srv://mongo_user:mmwp6FJ39lK7iAhE@cluster0.28agz.mongodb.net/db?retryWrites=true&w=majority"
client = pymongo.MongoClient(CONN)
db = client.mars



def scrape():

	executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
	browser = Browser('chrome', **executable_path)


	# Scrape title and paragraph from Mars Page
	url="https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
	browser.visit(url)


	html=browser.html
	soup=BeautifulSoup(html, "html.parser")

	news=soup.find("li", class_ = "slide")
	news_title=news.find("div", class_ = "content_title").text

	p=soup.find("li", class_ = "slide")
	news_p=p.find("div", class_ = "article_teaser_body").text

	

	# Scrape featured image

	url="https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
	browser.visit(url)

	browser.click_link_by_id("full_image")

	browser.click_link_by_partial_text('more info')

	html=browser.html
	soup=BeautifulSoup(html, "html.parser")

	featured_img=soup.select_one("figure", class_ = "lede")

	img_tag = featured_img.find("a").get("href")

	# concat with web url nasa.gov
	featured_image= "https://www.jpl.nasa.gov"+img_tag
	featured_image=[featured_image]

	html=browser.html
	soup=BeautifulSoup(html, "html.parser")



	# Scrape Mars table
	url="https://space-facts.com/mars/"
	browser.visit(url)

	table1=soup.find("table", class_ = "tablepress tablepress-id-p-mars")
	# table=table1.find("tbody").text
	table1


	# Hemisphere

	executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
	browser = Browser('chrome', **executable_path)

	html=browser.html
	soup=BeautifulSoup(html, "html.parser")

	# hem1
	url="https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced"
	browser.visit(url)
	hem1=browser.find_link_by_partial_text('Sample')[0]['href']

	# hem2
	url="https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced"
	browser.visit(url)
	hem2=browser.find_link_by_partial_text('Sample')[0]['href']

	# hem3
	url="https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced"
	browser.visit(url)
	hem3=browser.find_link_by_partial_text('Sample')[0]['href']

	# hem4
	url="https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced"
	browser.visit(url)
	hem4=browser.find_link_by_partial_text('Sample')[0]['href']

	hemispheres=[hem1, hem2, hem3, hem4]
	

	mars_dict = {}
	mars_dict = {
		"news_title": news_title,
		"news_p": news_p,
		"featured_img": featured_img,
		"hemispheres": hemispheres
	}

	db.mars.drop()
	db.mars.insert_one(mars_dict)
	return mars_dict

