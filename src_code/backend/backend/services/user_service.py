from backend.models.user import User
from backend.schemas.user import UserCreate

class UserService:
    def create_user(self, user: UserCreate):
        new_user = User(username=user.username, email=user.email, password=user.password)
        # save to database
        return new_user
