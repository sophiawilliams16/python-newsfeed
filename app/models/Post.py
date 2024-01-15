from datetime import datetime
from app.db import Base
from .Vote import Vote
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, select, func
from sqlalchemy.orm import relationship, column_property

class Post(Base):
  __tablename__ = 'posts'
  id = Column(Integer, primary_key=True)
  title = Column(String(100), nullable=False)
  post_url = Column(String(100), nullable=False)
  user_id = Column(Integer, ForeignKey('users.id'))
  created_at = Column(DateTime, default=datetime.now)
  updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
  user = relationship('User')
  # deleting post from db also deletes associated comments/votes 
  comments = relationship('Comment', cascade='all,delete')
  votes = relationship('Vote', cascade='all,delete')
  # Define vote_count as a regular column
  vote_count = Column(Integer, default=0)
  # Calculate vote_count dynamically using a @property method
  @property
  def calculate_vote_count(self):
    return len(self.votes)
