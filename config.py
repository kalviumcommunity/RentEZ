# Importing the required libraries
from decouple import config
from pymongo import MongoClient

class MongoConfig:
    def __init__(self):
        self.client = MongoClient(config('MONGO_URI'))