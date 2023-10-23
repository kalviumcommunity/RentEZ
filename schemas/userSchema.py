# Defining a schema for the user model
def userEntity(user) -> dict:
    return {
        "id": str(user["_id"]),
        "username": user["username"],
        "email": user["email"],
        "password": user["password"],
        "role": user["role"],
        "first_name": user["f_name"],
        "last_name": user["l_name"],
    }