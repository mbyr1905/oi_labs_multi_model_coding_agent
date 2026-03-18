from fastapi import APIRouter, Depends
from schemas.user import UserCreate
from services.user_service import UserService

router = APIRouter()

@router.post('/register')
def register_user(user: UserCreate):
    user_service = UserService()
    new_user = user_service.create_user(user)
    return new_user