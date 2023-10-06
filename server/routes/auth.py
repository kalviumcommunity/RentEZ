# Importing required libraries
from fastapi import APIRouter

# Importing required modules from files
from models.userModel import Renter #Importing the models
from controllers.userController import post_renter, hash_password, get_user #Importing the controller functions

# Creating a router object
router = APIRouter()

# Defining routes
@router.post("/register/renter")
def register_user(user: Renter):
    user.password = hash_password(user.password)
    post_renter(user.model_dump())
    return {"message": "User created successfully"}

@router.get("/register/{id}")
def get_user(id):
    return get_user(id)