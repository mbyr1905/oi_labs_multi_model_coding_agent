from fastapi import APIRouter, Depends
from backend.services import UserService

router = APIRouter()

@router.get("/admin")
def get_admin():
    user_service = UserService()
    admin = user_service.get_admin()
    return admin
