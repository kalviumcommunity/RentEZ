from decouple import config
from datetime import datetime, timedelta
import jwt
from fastapi import HTTPException

SECRET_KEY = config('JWT_SECRET')
ALGORITHM = config('JWT_ALGORITHM')
EXP_TIME = float(config('JWT_EXP_MINUTES'))

def token_dict(token):
    return {'token': token}

def create_token(user):
    payload = {
        'user_id': user['id'],
        'role': user['role'],
        'exp': datetime.utcnow() + timedelta(minutes=EXP_TIME),
    }

    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return token_dict(token)

def verify_token(token: str):
    print(token)
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload if datetime.fromtimestamp(payload['exp']) >= datetime.utcnow() else None
    except:
        raise HTTPException(status_code=401, detail="Invalid Token")
