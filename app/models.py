from datetime import datetime
from sqlalchemy import Column, DateTime, Integer, String, Boolean

from db import Base


# Table models
class TodoItem(Base):
 
    __tablename__ = "todo_items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255))
    description = Column(String(255))

    created_at: str = Column(DateTime,  default=datetime.now())
    updated_at: str = Column(DateTime,  default=datetime.now())
    completed = Column(Boolean, default=False)

    def __repr__(self):
       
        return f'{self.id}. {self.title}'
