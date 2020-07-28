from database.database_manager import base, Session, engine
from sqlalchemy import Column, Integer, String, Binary
from passlib.hash import argon2
import os


class User(base):
    __tablename__ = 'user'

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    username = Column('username', String)
    password_hash = Column('password_hash', String)
    salt = Column('salt', Binary)


def add(user: User) -> None:
    session = Session()

    if exists(user.username):
        print("ERROR: Trying to add user that already exists")
        return

    session.add(user)

    session.commit()
    session.close()


def valid_login(username: str, password: str) -> bool:
    if not exists(username):
        return False

    # Get salt and hash from database
    session = Session()
    user = session.query(User).filter_by(username=username).scalar()
    session.close()

    salt = user.salt
    password_hash = user.password_hash
    return argon2.using(salt=salt).verify(password, password_hash)


def exists(username: str) -> bool:
    session = Session()

    user_exists = session.query(User.id).filter_by(username=username).scalar() is not None

    session.close()
    return user_exists


def hash_password(password: str) -> tuple:
    """
    Returns a tuple containing the hash and the salt
    """
    salt = os.urandom(32)
    pw_hash = argon2.using(salt=salt).hash(password)
    return pw_hash, salt

