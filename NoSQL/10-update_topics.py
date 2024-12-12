#!/usr/bin/env python3
""" Updates a document """
from pymongo import MongoClient


client = MongoClient("mongodb://localhost:27017/")
db = client.mydatabase
mongo_collection = db.school

def update_topics(mongo_collection, name, topics):
    """ Adds new stuff and updates the topic """
    return mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
