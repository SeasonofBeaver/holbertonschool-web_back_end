#!/usr/bin/env python3
""" Stats about Nginx """

from pymongo import MongoClient


if __name__ == "__main__":
    """ prints stats about Nginx logs """

    client = MongoClient("mongodb://127.0.0.1:27017")
    collection = client.logs.nginx

    print(f"{collection.count_documents({})} logs\nMethods:")

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    dictionary = {}

    for method in methods:
        dictionary[method] = collection.count_documents({"method": method})

    for method, logs in dictionary.items():
        print(f"\tmethod {method}: {logs}")

    statusCheck = collection.count_documents(
        {"method": "GET", "path": "/status"}
    )
    print(f"{statusCheck} status check")
