from sqlalchemy import create_engine, Column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class YourItemModel(Base):
    __tablename__ = 'yourtable'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    field1 = Column(String(50))
    field2 = Column(String(50))
    field3 = Column(String(50))

def db_connect(database):
    return create_engine(database)

def create_table(engine):
    Base.metadata.create_all(engine)
