from typing import Optional
from pydantic import BaseModel



class TodoItemResponse(BaseModel):
    id: int
    



class TodoItemCreate(BaseModel):
    id: Optional[int]
    title: str
    description: str
    completed: Optional[bool] = False
    

class TodoItemUpdate(BaseModel):
    id: int


