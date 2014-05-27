from usersvc.lib.users import encrypt_password, verify_password

class User():
    def __init__(self, user_id, username):
        self.uid = user_id
        self.username = username

    @property
    def password(self):
        return self.password_digest
    
    @password.setter
    def password(self, value):
        self.password_digest = encrypt_password(value)

    def verify_password(self, password):
        return verify_password(password, self.password_digest)
