from pymongo import MongoClient
import config

client = MongoClient(config.MONGO_URI)
db = client["soccer_db"]
matches_collection = db["matches"]
