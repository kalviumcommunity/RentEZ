from decouple import config
from pymongo import MongoClient

conn = MongoClient(config("MONGO_URI"))