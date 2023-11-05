from fastapi import APIRouter, Header, HTTPException, Depends

from controllers.carController import getCars, createHatchback
from models.carModel import Hatchback
from controllers.authController import verify_token

router = APIRouter()

@router.get("/")
def get_cars():
    return getCars()

def token_from_header(authorization: str = Header(None)):
    if authorization is None or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Invalid Authorization Header")
    
    token = authorization.replace("Bearer ", "")
    return verify_token(token)

@router.post("/hatchback")
def create_hatchback(car: Hatchback, token: dict = Depends(token_from_header)):
    if token['role'] != 'rental_owner':
        raise HTTPException(status_code=401, detail="Unauthorized")
    return createHatchback(car.model_dump())