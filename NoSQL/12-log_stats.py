#!/usr/bin/env python3
""" Stats about Nginx """
from pymongo import MongoClient


def log_stats():
    """ prints stats about Nginx logs """

    client = MongoClient('localhost', 27017)
    db = client.logs
    collection = db.nginx
    
    total_logs = collection.count_documents({})
    print(f"{total_logs} logs")

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    
    for method in methods:
        methodcount = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {methodcount}")
    
    statusCheck = collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{statusCheck} status check")

if __name__ == "__main__":
    log_stats()