from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from datetime import datetime

from database import Base



class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    
    
class Message(Base):
    __tablename__ = "messages"
    
    id = Column(Integer, primary_key=True)
    sender_id = Column(Integer, ForeignKey("users.id"))
    receiver_id = Column(Integer, ForeignKey("users.id"))
    content = Column(String, nullable=False)
    timestamp = Column(DateTime, default=datetime.now)