# Importing required libraries
from fastapi import APIRouter

# Importing required modules from files
from models.userModel import Renter, RentalOwner, LoginCred #Importing the models
from controllers.userController import createRenter, createRentalOwner, hashPassword, getUserById, loginUser #Importing the controller functions

# Creating a router object
router = APIRouter()

# Defining routes
@router.post("/register/renter")
def register_renter(user: Renter):
    user.password = hashPassword(user.password)
    return createRenter(user.model_dump())

@router.post("/register/rental-owner")
def register_renter(user: RentalOwner):
    user.password = hashPassword(user.password)
    return createRentalOwner(user.model_dump())

@router.post("/login")
def login_user(creds: LoginCred):
    return loginUser(creds)

@router.get("/register/{id}")
def get_user_by_id(id):
    return getUserById(id)