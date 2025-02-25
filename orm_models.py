#!/usr/bin/env python3

from sqlalchemy import Column, Integer, String, Boolean
from database import Base

class Item(Base):
    __tablename__ = "tablename"

    id = Column(Integer, primary_key=True, autoincrement=True)
    task = Column(String, nullable=False)
    isDone = Column(Boolean, nullable=False)

    def __repr__(self):
        return f"<Item(task='{self.task}', isDone={self.isDone})>"
    
# from database import engine
# Base.metadata.create_all(engine)