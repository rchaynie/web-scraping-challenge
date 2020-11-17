import pandas as pd
import requests
from bs4 import BeautifulSoup
import pprint
from splinter import Browser
from selenium import webdriver


!which chromedriver

executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
browser = Browser('chrome', **executable_path)




driver=webdriver.Chrome('/usr/local/bin/chromedriver')


# Scrape title and paragraph from Mars Page
url = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"


driver.get("https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest")


### HOW DO I SAVE TARGETED ELEMENTS. DO I JUST WRITE THEM OUT MANUALLY? 
news_title=driver.find_element_by_xpath("""//*[@id="page"]/div[3]/div/article/div/section/div/ul/li[1]/div/div/div[2]/a""").click()


news_p=driver.find_element_by_xpath("""//*[@id="page"]/div[3]/div/article/div/section/div/ul/li[1]/div/div/div[3]""").click()



# def get_html(url):
#     driver=webdriver.Chrome('/usr/local/bin/chromedriver')
#     driver.get(url)
#     html=driver.page_source
#     driver.close()
#     return html
# html=get_html(url)
# print(html)


# Scrape featured image

driver.get("https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars")



driver.find_element_by_xpath("//*[@id='full_image']").click()


#### HOW DO I NAVIGATE TO A DOWNLOADABLE IMAGE? DO I GO VIA SHARE, PRINT?  

driver.find_element_by_xpath("//*[@id='fancybox-lock']/div/div[1]/img").click()



# Scrape Mars Facts