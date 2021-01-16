from typing import Union

from app.application.models.user import UserModel
from app.application.protocols.user_repository import UserRepository
from app.infra.db.fake_db.data_sources import users


class FakeUserRepository(UserRepository):
    def find_by_email(self, email: str) -> Union[UserModel, None]:
        for user in users:
            if user.get('email') == email:
                return UserModel(**user)
        return None
