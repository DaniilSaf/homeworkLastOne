from sqlalchemy import Column,Integer,Text,DateTime,String
from datetime import datetime
from database import Base

class Task(Base):
    __tablename__ = "task"
    id = Column(Integer,primary_key=True,index=True)
    title = Column(Text,nullable=False)
    description = Column(Text,nullable=True)
    status = Column(String,nullable=False,default='pending')
    priority = Column(Integer,nullable=False,default=1)# важность чем больше тем важнее
    created_at = Column(DateTime,nullable=False,default=datetime.utcnow)
