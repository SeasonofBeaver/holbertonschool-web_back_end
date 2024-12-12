#!/usr/bin/env python3
""" Stats about Nginx """

from pymongo import MongoClient


def nginx_stats() -> None:
    """prints stats about Nginx logs"""
    try:
        with MongoClient("mongodb://localhost:27017/") as client:
            db = client.logs
            collection = db.nginx

            total_logs = collection.count_documents({})
            print(f"{total_logs} logs")

            methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
            print("Methods:")
            for method in methods:
                method_count = collection.count_documents({"method": method})
                print(f"\tmethod {method}: {method_count}")

            status_check = collection.count_documents({"method": "GET", "path": "/status"})
            print(f"{status_check} status check")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    nginx_stats()
