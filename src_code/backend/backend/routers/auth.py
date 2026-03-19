from fastapi import APIRouter, Depends
from backend.services.user_service import UserService
outer = APIRouter()

@router.post("/register")
def register(user: UserCreate):
    user_service = UserService()
    new_user = user_service.create_user(user)
    return new_user
