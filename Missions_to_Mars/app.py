from scrape_mars import scrape
import os
from flask import Flask, jsonify, render_template
from flask_pymongo import PyMongo



# CONN = os.getenv("CONN")
# client = pymongo.MongoClient(CONN)
# db = client.mars

# CONN = os.getenv("mongodb+srv://mongo_user:zX6r9wmhxyvFvuk@cluster0.28agz.mongodb.net/mars?retryWrites=true&w=majority")
# client = pymongo.MongoClient(CONN)
# db.client.mars

app = Flask(__name__)



@app.route("/")
def main():
    mars = db.mars.find_one()
    print(mars)
    return render_template("index.html")

@app.route("/scraping")
def scraping():
    mars_dict = scrape()
    return "Scraping successful! To view your data, visit {{main}}"

if __name__ == "__main__":
    app.run(debug=True)

