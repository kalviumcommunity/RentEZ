from pydantic import BaseModel

class User(BaseModel):
    def __init__(self, username: str, email: str, password: str, role: str, f_name: str = None, l_name: str = None) -> None:
        # Compulsory fields
        self.username = username
        self.email = email
        self.password = password
        
        # Optional fields
        self.f_name = f_name
        self.l_name = l_name

        self.role = role

class Renter(User):
    def __init__(self, username: str, email: str, password: str, f_name: str = None, l_name: str = None) -> None:
        self.role = "renter"
        super().__init__(username, email, password, self.role, f_name, l_name)

class RentalOwner(User):
    def __init__(self, username: str, email: str, password: str, f_name: str = None, l_name: str = None) -> None:
        self.role = "rentalOwner"
        super().__init__(username, email, password, self.role, f_name, l_name)

class Admin(User):
    def __init__(self, username: str, email: str, password: str, f_name: str = None, l_name: str = None) -> None:
        self.role = "admin"
        super().__init__(username, email, password, self.role, f_name, l_name)