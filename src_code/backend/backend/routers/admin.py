from fastapi import APIRouter, Depends
outer = APIRouter()

@router.get("/admin")
def admin_panel():
    # admin panel logic
    pass
