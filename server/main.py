# Importing required libraries
from fastapi import FastAPI

# Importing required modules from files
from routes.auth import router as auth_router

# Creating a FastAPI object
app = FastAPI()

# Defining routes
@app.get("/")
def root():
    return {"message": "Welcome to RentEZ"}

# Including the routers
app.include_router(auth_router, prefix="/auth")