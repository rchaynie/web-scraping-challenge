import pandas as pd
import requests
from bs4 import BeautifulSoup
import pprint
from splinter import Browser
from selenium import webdriver




def scrape():

		### NEWS STORY###
	executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
	browser = Browser('chrome', **executable_path)

	url="https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
	browser.visit(url)

	html=browser.html
	soup=BeautifulSoup(html, "html.parser")

	news=soup.find("li", class_ = "slide")
	news_title=news.find("div", class_ = "content_title").text
	news_title

	p=soup.find("li", class_ = "slide")
	news_p=p.find("div", class_ = "article_teaser_body").text
	news_p

	time.sleep(2)

		###FEATURED IMAGE###
	executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
	browser = Browser('chrome', **executable_path)

	url="https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
	browser.visit(url)

	browser.click_link_by_id("full_image")

	browser.click_link_by_partial_text('more info')

	html=browser.html
	soup=BeautifulSoup(html, "html.parser")

	featured_img=soup.select_one("figure", class_ = "lede")

	img_tag = featured_img.find("a").get("href")

	featured_image= "https://www.jpl.nasa.gov"+img_tag


	time.sleep(2)
		###TABLE###
	html=browser.html
	soup=BeautifulSoup(html, "html.parser")

	url="https://space-facts.com/mars/"
	browser.visit(url)

	table1=soup.find("table", class_ = "tablepress tablepress-id-p-mars")
	table=table1.find("tbody").text
	table

	time.sleep(2)
		###HEMISPHERES###

	executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
	browser = Browser('chrome', **executable_path)

	html=browser.html
	soup=BeautifulSoup(html, "html.parser")


	url="https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced"
	browser.visit(url)
	hem1=browser.click_link_by_partial_text('Sample')

	url="https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced"
	browser.visit(url)
	hem2=browser.click_link_by_partial_text('Sample')

	url="https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced"
	browser.visit(url)
	hem3=browser.click_link_by_partial_text('Sample')


	url="https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced"
	browser.visit(url)
	hem4=browser.click_link_by_partial_text('Sample')


	time.sleep(2)
	browser.quit


	result= {
		"new_title": news_title,
		"news_info": news_p,
		"featured_img": featured_img,
		"table": table,
		"hem1": hem1,
		"hem2": hem2,
		"hem3": hem3,
		"hem4": hem4,
		}


	return result

