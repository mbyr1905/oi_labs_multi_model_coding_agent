from fastapi import APIRouter, Depends
from backend.services import UserService
from backend.schemas import UserCreate

router = APIRouter()

@router.post("/register")
def register_user(user: UserCreate):
    user_service = UserService()
    new_user = user_service.create_user(user)
    return new_user
