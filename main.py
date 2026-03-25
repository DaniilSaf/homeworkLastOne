from fastapi import FastAPI,Depends,HTTPException,status
from functools import lru_cache
from sqlalchemy.orm import Session
import models
import crud
import schemas
from database import engine, Sessionlocal
app=FastAPI()
models.Base.metadata.create_all(bind=engine)
def get_db():
    db = Sessionlocal()
    try:
        yield db
    finally:
        db.close()
@app.get("/")
def read_root():
    return {"message":"This is the root of the API"}



@app.post("/tasks",response_model=schemas.Task)
def create_task(task: schemas.TaskCreate,db: Session=Depends(get_db)):
    return crud.create_task(db,task)



@app.get("/tasks",response_model=list[schemas.Task])
def read_tasks(sort_by: str | None = None,db: Session=Depends(get_db)):
    return crud.get_tasks(db,sort_by)



@app.get("/tasks/{task_id}",response_model=schemas.Task)
def read_task(task_id:int,db:Session=Depends(get_db)):
    task = crud.get_task(db,task_id)
    if task is None:
        raise HTTPException(status_code=404,detail="Such a task does not exist")
    return task



@app.put("/tasks/{task_id}",response_model=schemas.Task)
def update_task(task_id: int,task:schemas.TaskCreate,db:Session=Depends(get_db)):
    updated_task = crud.update_task(db,task_id,task)
    if updated_task is None:
        raise HTTPException(status_code=404,detail="Such a task does not exist")
    return updated_task



@app.delete("/tasks/{task_id}")
def delete_task(task_id: int, db: Session=Depends(get_db)):
    deleted_task = crud.delete_task(db, task_id)
    if deleted_task is None:
        raise HTTPException(status_code=404, detail="Such a task does not exist")
    return {"message": "Task deleted"}


@app.get("/tasks/top/{n}",response_model=list[schemas.Task])
def read_top_tasks(n:int,db:Session=Depends(get_db)):
    return crud.get_top_tasks(db, n)

@app.get("/tasks/search/",response_model=list[schemas.Task])
def search_tasks(query: str,db:Session=Depends(get_db)):
    return crud.search_tasks(db, query)
