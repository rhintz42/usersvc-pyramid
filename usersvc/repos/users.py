from usersvc.db_tables import DBSession
from usersvc.db_tables.users import UsersTable
from usersvc.models.users import User

class UsersRepo:
    def __init__(self, service=None):
        self.service = service

    def get_user_by_id(self, user_id):
        result = DBSession.query(UsersTable).filter(UsersTable.uid == user_id)
        try:
            user = build_user(result.one())
        except:
            user = None
        return user

    def get_all(self):
        users = DBSession.query(UsersTable).all()
        return [build_user(u) for u in users]

    def update_by_id(self, user_id, user_model):
        users = DBSession.query(UsersTable).all()
        return users

def build_user(user_info):
    user = User(user_info.uid, user_info.username)
    user.email = user_info.email
    user.is_public = user_info.is_public
    user.name_first = user_info.name_first
    user.name_last = user_info.name_last
    user.password_digest = user_info.password_digest
    user.picture_url = user_info.picture_url
    user.salt = user_info.salt
    user.url = user_info.url
    return user
