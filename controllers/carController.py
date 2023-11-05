# Importing required libraries
from decouple import config
from fastapi import HTTPException

# Importing required modules from files
from models.carModel import Hatchback #Importing the models
from config import MongoConfig #Importing the config to get the access to the database
from schemas.carSchema import carEntity #Importing the schema to convert the data from the database to the model

# Getting the environment variables
DB_NAME = config('DB_NAME')
COLLECTION = config('COLLECTION2')

def getCars():
    client = MongoConfig().client
    db = client.get_database(DB_NAME)
    collection = db[COLLECTION]

    cars = []
    for car in collection.find():
        cars.append(carEntity(car))

    return cars

def createHatchback(car: Hatchback):
    client = MongoConfig().client
    db = client.get_database(DB_NAME)
    collection = db[COLLECTION]
    collection.insert_one(car)