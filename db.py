import pymongo
import sqlite3

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
DocDB   = myclient["{0}"]
AuthDB  = sqlite3.connect("./data/auth.db", check_same_thread=False)