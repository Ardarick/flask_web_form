from datetime import datetime

from sqlalchemy import Column, String, Integer, DateTime

from app.models.meta import Base


class FormData(Base):
    __tablename__ = 'form_data'

    id = Column(Integer, primary_key=True)
    name = Column(String(length=16))
    creation_date = Column(DateTime)

    def __init__(self, name):
        self.name = name
        self.creation_date = datetime.now()
