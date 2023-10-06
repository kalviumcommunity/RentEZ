# Importing required libraries
from decouple import config
import bcrypt
from bson import ObjectId

# Importing required modules from files
from models.userModel import Renter #Importing the models
from config import MongoConfig #Importing the config to get the access to the database
from schemas.userSchema import userEntity #Importing the schema to convert the data from the database to the model

# Getting the environment variables
DB_NAME = config('DB_NAME')
COLLECTION = config('COLLECTION1')

# Defining the controller functions
def hash_password(password: str) -> str:
    salt = bcrypt.gensalt(8)
    hashed_password = bcrypt.hashpw(password.encode(), salt).decode()
    return hashed_password

def post_renter(user: Renter):
    client = MongoConfig().client
    db = client.get_database(DB_NAME)
    collection = db[COLLECTION]
    collection.insert_one(user)

def get_user(id):
    client = MongoConfig().client
    db = client.get_database(DB_NAME)
    collection = db[COLLECTION]
    return userEntity(collection.find_one({"_id": ObjectId(id)}))