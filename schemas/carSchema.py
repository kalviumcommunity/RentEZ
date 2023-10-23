from bson import ObjectId

def carEntity(car) -> dict:
    return {
        "id": str(car["_id"]),
        "company": car["company"],
        "model": car["model"],
        "color": car["color"],
        "fuel_type": car["fuel_type"],
        "transmission": car["transmission"],
        "no_of_seats": car["no_of_seats"],
        "price": car["price"],
        "mileage": car["mileage"],
        "owner_id": car["owner_id"],
    }