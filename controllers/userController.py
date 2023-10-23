# Importing required libraries
from decouple import config
import bcrypt
from bson import ObjectId
from fastapi import HTTPException

# Importing required modules from files
from models.userModel import Renter, RentalOwner, LoginCred #Importing the models
from config import MongoConfig #Importing the config to get the access to the database
from schemas.userSchema import userEntity #Importing the schema to convert the data from the database to the model
from controllers.authController import create_token

# Getting the environment variables
DB_NAME = config('DB_NAME')
COLLECTION = config('COLLECTION1')

# Defining the controller functions
def hashPassword(password: str) -> str:
    salt = bcrypt.gensalt(8)
    hashed_password = bcrypt.hashpw(password.encode(), salt).decode()
    return hashed_password

def createRenter(user: Renter):
    client = MongoConfig().client
    db = client.get_database(DB_NAME)
    collection = db[COLLECTION]

    if collection.find_one({"email": user['email']}):
        raise HTTPException(status_code=409, detail="Email already registered")
    elif collection.find_one({"username": user['username']}):
        raise HTTPException(status_code=409, detail="Username already taken")

    collection.insert_one(user)
    return create_token(userEntity(user))

def createRentalOwner(user: RentalOwner):
    client = MongoConfig().client
    db = client.get_database(DB_NAME)
    collection = db[COLLECTION]

    if collection.find_one({"email": user['email']}):
        raise HTTPException(status_code=409, detail="Email already registered")
    elif collection.find_one({"username": user['username']}):
        raise HTTPException(status_code=409, detail="Username already taken")

    collection.insert_one(user)
    return create_token(userEntity(user))

def loginUser(creds: LoginCred):
    client = MongoConfig().client
    db = client.get_database(DB_NAME)
    collection = db[COLLECTION]

    user = userEntity(collection.find_one({"$or": [{"email": creds.email_or_username}, {"username": creds.email_or_username}]}))
    try:
        if user:
            if bcrypt.checkpw(creds.password.encode(), user['password'].encode()):
                return create_token(user)
            else:
                raise HTTPException(status_code=401, detail="Invalid credentials")
        else:
            raise HTTPException(status_code=404, detail="User Not Found")
    except:
        raise

def getUserById(id):
    client = MongoConfig().client
    db = client.get_database(DB_NAME)
    collection = db[COLLECTION]
    return userEntity(collection.find_one({"_id": ObjectId(id)}))