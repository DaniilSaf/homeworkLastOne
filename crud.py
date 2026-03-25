from sqlalchemy.orm import Session
import models
import schemas
def create_task(db:Session,task:schemas.TaskCreate):
    task=models.Task(title=task.title,description=task.description,status=task.status,priority=task.priority)
    db.add(task)
    db.commit()
    db.refresh(task)
    return task
def get_tasks(db: Session, sort_by: str | None = None):
    query = db.query(models.Task)
    if sort_by=="title":
        query=query.order_by(models.Task.title)
    elif sort_by=="status":
        query=query.order_by(models.Task.status)
    elif sort_by=="created_at":
        query=query.order_by(models.Task.created_at)
    return query.all()
def get_task(db: Session, task_id: int):
    return db.query(models.Task).filter(models.Task.id == task_id).first()



def update_task(db: Session, task_id: int, task_data: schemas.TaskCreate):
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if task is None:
         return None
    task.title=task_data.title
    task.description=task_data.description
    task.status=task_data.status
    task.priority=task_data.priority
    db.commit()
    db.refresh(task)
    return task

def delete_task(db:Session,task_id:int):
    task=db.query(models.Task).filter(models.Task.id==task_id).first()
    if task is None:
        return None
    db.delete(task)
    db.commit()
    return task
def get_top_tasks(db:Session,n:int):
    return db.query(models.Task).order_by(models.Task.priority.desc()).limit(n).all()

def search_tasks(db: Session, query: str):
    return db.query(models.Task).filter((models.Task.title.contains(query))|(models.Task.description.contains(query))).all()