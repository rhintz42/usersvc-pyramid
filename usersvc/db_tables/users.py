from usersvc.db_tables import Base, DBSession

from sqlalchemy import (
    Boolean,
    Column,
    Integer,
    Text,
    )

class UsersTable(Base):
    __tablename__ = 'users'
    email = Column(Text)
    is_public = Column(Boolean)
    name_first = Column(Text)
    name_last = Column(Text)
    password_digest = Column(Text)
    picture_url = Column(Text)
    salt = Column(Integer)
    uid = Column(Integer, primary_key=True)
    url = Column(Text)
    username = Column(Text, unique=True)
