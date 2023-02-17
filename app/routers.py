from operator import itemgetter
from typing import List
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

import schemas
from db import get_db
from models import TodoItem


router = APIRouter(tags=["Todo Items"])


@router.get("/todo-items/", response_model=List[schemas.TodoItemResponse])
async def get_todo_items(db: Session = Depends(get_db)):

    query = db.query(TodoItem).all()
    result = []
    for item in query:
        result.append({"id": int(item.__repr__().split(".")[0])})
    print(result)
    return result


@router.get("/todo-items/{todo_item_id}", response_model=schemas.TodoItemResponse)
async def get_todo_item(todo_item_id: int, db: Session = Depends(get_db)):
    
    pass


@router.post("/todo-items/", response_model=schemas.TodoItemResponse, status_code=status.HTTP_201_CREATED)
async def create_todo_item(todo_item: schemas.TodoItemCreate, db: Session = Depends(get_db)):
    
    title, description, completed = itemgetter(
        "title", "description", "completed")(todo_item.dict())

    new_todo = TodoItem(
        title=title, description=description, completed=completed)

    db.add(new_todo)
    db.commit()
    new_id = new_todo.__repr__().split(".")[0]
    return {"id": int(new_id)}


@router.put("/todo-items/{todo_item_id}", response_model=schemas.TodoItemResponse)
async def update_todo_item(todo_item_id: int, todo_item: schemas.TodoItemUpdate, db: Session = Depends(get_db)):
    
    pass


@router.delete("/todo-items/{todo_item_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo_item(todo_item_id: int, db: Session = Depends(get_db)):
   
    item_to_delete = db.query(TodoItem).get({"id": todo_item_id})
    db.delete(item_to_delete)
    db.commit()
