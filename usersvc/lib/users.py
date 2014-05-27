import bcrypt

def encrypt_password(password):
    password_digest = bcrypt.hashpw(password, bcrypt.gensalt(10))
    return password_digest

def verify_password(password, password_digest):
    return bcrypt.hashpw(password, password_digest) == password_digest
