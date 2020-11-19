from scrape_mars import scrape

import os

from flask import Flask, jsonify
import pymongo

# CONN = os.getenv("mongodb+srv://mongo_user:zX6r9wmhxyvFvuk@cluster0.28agz.mongodb.net/mars?retryWrites=true&w=majority")
# client = pymongo.MongoClient(CONN)
# db.client.mars

app = Flask(__name__)

@app.route("/")
def main():
    return "welcome"

@app.route("/scrape")
def scrape():
    mars = mongo.db.mars
    mars_data = scrape_mars.scrape_all()
    mars.update({}, mars_data, upsert=True)
    return "Scraping successful!"


if __name__ == "__main__":
    app.run(debug=True)

