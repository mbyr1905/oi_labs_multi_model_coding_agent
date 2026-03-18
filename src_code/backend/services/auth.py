from models import User
from schemas.user import UserCreate
from database import SessionLocal

def authenticate_user(username: str, password: str):
    db = SessionLocal()
    user = db.query(User).filter(User.username == username).first()
    if not user or not user.password == password:
        return None
    return user

def create_user(user: UserCreate):
    db = SessionLocal()
    new_user = User(username=user.username, email=user.email, password=user.password)
    db.add(new_user)
    db.commit()