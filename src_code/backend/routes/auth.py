from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from schemas.user import UserCreate
from services.auth import authenticate_user, create_user

router = APIRouter()

@router.post('/login')
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        return {'error': 'Invalid username or password'}
    return {'access_token': user.username, 'token_type': 'bearer'}

@router.post('/register')
async def register(user: UserCreate):
    create_user(user)
    return {'message': 'User created successfully'}