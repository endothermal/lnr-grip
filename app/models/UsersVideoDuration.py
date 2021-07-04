from sqlalchemy import Column, Integer, String
from .. import db

class UsersVideoDuration(db.Model):

    __tablename__ = 'users_video_durations'
    __table_args__ = {'extend_existing': True}
    user_id = Column(Integer, primary_key=True)
    total_duration = Column(Integer)



