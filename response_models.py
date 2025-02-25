from pydantic import BaseModel

class ItemBase(BaseModel):
    task: str
    isDone: bool = False

class ItemCreate(ItemBase):
    pass

class Item(ItemBase):
    id: int

    class Config:
        from_attributes = True