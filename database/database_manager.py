import sqlalchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import settings


engine = sqlalchemy.create_engine(settings.SQLALCHEMY_DATABASE_URI, echo=True)
base = declarative_base()
Session = sessionmaker(bind=engine)


def init_db() -> None:
    base.metadata.create_all(bind=engine)

