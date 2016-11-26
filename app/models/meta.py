# coding=utf-8
from sqlalchemy import MetaData, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

engine = create_engine(name_or_url='sqlite:///db.sqlite')

metadata = MetaData(
    bind=engine
)

session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)

Base = declarative_base(bind=engine, metadata=metadata)
