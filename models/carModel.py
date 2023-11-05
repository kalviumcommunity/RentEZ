from pydantic import BaseModel, Field

class price_per_unit(BaseModel):
    hour: int = Field(default=None)
    day: int = Field(default=None)
    week: int = Field(default=None)

class Cars(BaseModel):
    company: str = Field(default=None)
    model: str = Field(default=None)
    fuel_type: str = Field(default=None)
    color: str = Field(default=None)
    transmission: str = Field(default=None)
    mileage: int = Field(default=None)
    price: price_per_unit
    no_of_seats: int = Field(default=None)
    owner_id: str = Field(default=None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class Hatchback(Cars):
    type: str = "hatchback"

class Sedan(Cars):
    type: str = "sedan"

class SUV(Cars):
    type: str = "suv"

class MUV(Cars):
    type: str = "muv"

class Luxury(Cars):
    type: str = "luxury"
