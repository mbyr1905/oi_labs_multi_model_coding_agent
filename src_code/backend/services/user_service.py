from models.user import User
from schemas.user import UserCreate

class UserService:
    def create_user(self, user: UserCreate):
        new_user = User(username=user.username, email=user.email, password=user.password)
        return new_user