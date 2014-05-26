from usersvc.db_tables import DBSession
from usersvc.db_tables.users import UsersTable
from usersvc.models.users import User

from sqlalchemy import update
import transaction

class UsersRepo:
    def __init__(self, service=None):
        self.service = service

    # Change to `get_by_id`
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

    # TODO: Need to make sure can't update username to one that already exists
    def update_by_id(self, user_id, user_info):
        try:
            user = DBSession.query(UsersTable).filter(UsersTable.uid ==
                    user_id).update({'username':user_info['username']})
            transaction.commit()
        except:
            return {'status': '1', 'data': 'Username Exists'}
            
        return {'status': '0', 'data': 'Update User Successful'}

    # TODO: What should I return from this function?
    #           * Need to be able to say whether creating successful or not
    # TODO: Am I adding objects correctly? If I do this, it gets committed,
    #           which makes it harder todo integration tests
    def create(self, user_info):
        user = UsersTable(username=user_info['username'])
        status = DBSession.add(user)
        try:
            transaction.commit()
        except:
            return {'status': '1', 'data': 'Username Exists'}

        return {'status': '0', 'data': 'Create User Successful'}

    def delete(self, user_id):
        try:
            user = DBSession.query(UsersTable).filter(UsersTable.uid ==
                        user_id).one()
        except:
            return {'status': '2', 'data': 'No User Found'}

        try:
            status = DBSession.delete(user)
            transaction.commit()
        except:
            transaction.abort() # This seems necessary for the functional tests
                                #   to run
            return {'status': '1', 'data': 'Something Went Wrong'}

        return {'status': '0', 'data': 'Create User Successful'}

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
