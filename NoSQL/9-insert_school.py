#!/usr/bin/env python3
""" Inserts a document """

from pymongo import MongoClient


client = MongoClient("mongodb://localhost:27017/")
db = client.mydatabase
mongo_collection = db.school

def insert_school(mongo_collection, **kwargs):
    """ inserts new info into the collection """
    return mongo_collection.insert_one(kwargs).inserted_id
