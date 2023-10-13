# Importing required libraries
from pydantic import BaseModel

# Define User Model
class User(BaseModel):
    username: str
    email: str
    password: str
    f_name: str = None
    l_name: str = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

# Inheriting from User Model and creating a user type - Renter
class Renter(User):
    role: str = "renter"

# Inheriting from User Model and creating a user type - RentalOwner
class RentalOwner(User):
    role: str = "rental_owner"

# Inheriting from User Model and creating a user type - Admin
class Admin(User):
    role: str = "admin"