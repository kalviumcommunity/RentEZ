class User:
    def __init__(self, name: str, email: str, password: str):
        self.name = name
        self.email = email
        self.password = password

    def change_password(self, new_password):
        self.password = new_password

    def __repr__(self):
        return "User {}, email: {}, password: {}".format(self.name, self.email, self.password)
    
user1 = User(name="Arthur", email="arthur@gmail.com", password="1234")
print(user1)