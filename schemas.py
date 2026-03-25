from pydantic import BaseModel
from enum import Enum
from datetime import datetime
class StatusEnum(str,Enum):
    pending="pending"
    working="working"
    finished="finished"
class TaskBase(BaseModel):
    title: str
    description: str | None=None
    status: StatusEnum=StatusEnum.pending
    priority: int = 1

class TaskCreate(TaskBase):
    pass
class Task(TaskBase):
    id: int
    created_at: datetime
    class Config:
        orm_mode = True
