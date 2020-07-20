from database.database_manager import base, Session
from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.exc import IntegrityError


class Vocabulary(base):
    __tablename__ = 'vocabulary'

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    pinyin = Column('pinyin', String)
    character = Column('character', Text, unique=True)
    german = Column('german', String)


def add(vocab: Vocabulary) -> None:
    session = Session()

    session.add(vocab)
    try:
        session.commit()
    except IntegrityError:
        session.rollback()
    finally:
        session.close()


def get_all() -> list:
    session = Session()

    vocabs = session.query(Vocabulary).all()

    vocabs = [list(vocab.__dict__.values())[1:] for vocab in vocabs]

    session.close()
    return vocabs
