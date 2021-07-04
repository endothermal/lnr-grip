from sqlalchemy import Column, Integer, String
from .. import db

class VideoAction(db.Model):

    __tablename__ = 'video_actions'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True) #Added a primary key to this table
    user_id = Column(Integer)
    device = Column(String(35))
    action = Column(String(35))
    date_actioned = Column(Integer)



