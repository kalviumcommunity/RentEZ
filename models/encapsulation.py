class User:
    def __init__(self, username: str, email: str, password: str, f_name: str = None, l_name: str = None):
        self.username = username # Public data member
        self.__email = email # This and beyond are private data members
        self.__password = password
        self.__f_name = f_name
        self.__l_name = l_name

    def display(self):
        print(self.__username, self.__email, self.__password, self.__f_name, self.__l_name)

user = User("test", "test@gmail.com", "test123", "test", "test")
print(user.__email)