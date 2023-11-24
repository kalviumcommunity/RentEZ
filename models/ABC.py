from abc import ABC, abstractmethod

class User(ABC):
    @abstractmethod
    def display():
        pass

class Renter(User):
    def __init__(self, username: str, email: str, password: str, f_name: str = None, l_name: str = None):
        super().__init__(username, email, password, f_name, l_name)

    def display():
        print("Renter")

user = Renter()
# user.display()