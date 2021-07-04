from sqlalchemy import Column, Integer, Text, DateTime, String
from .. import db

class User(db.Model):

    __tablename__ = 'users'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True)
    first_name = Column(String(35))
    last_name = Column(String(35))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    deleted_at = Column(DateTime)

