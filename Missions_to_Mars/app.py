from ____ import ____

import os

from flask import Flask, jsonify
import pymongo

CONN = os.getenv(CONN="mongodb+srv://mongo_user:zX6r9wmhxyvFvuk@cluster0.28agz.mongodb.net/mars?retryWrites=true&w=majority")
client = pymongo.MongoClient(CONN)
db.client.mars