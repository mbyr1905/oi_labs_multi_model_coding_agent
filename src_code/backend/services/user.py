from backend.models import User
from backend.schemas import UserCreate

class UserService:
    def create_user(self, user: UserCreate):
        new_user = User(username=user.username, email=user.email, password=user.password)
        # save to database
        return new_user
    def get_seller(self):
        # retrieve seller from database
        return {}
    def get_admin(self):
        # retrieve admin from database
        return {}