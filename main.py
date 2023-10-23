# Importing required libraries
from fastapi import FastAPI

# Importing required modules from files
from routes.authRoutes import router as auth_router
from routes.carRoutes import router as car_router

# Creating a FastAPI object
app = FastAPI()

# Defining routes
@app.get("/")
def root():
    return {"message": "Welcome to RentEZ"}

# Including the routers
app.include_router(auth_router, prefix="/auth")
app.include_router(car_router, prefix="/cars")
