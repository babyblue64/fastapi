from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import getDb
import orm_models
import response_models

app = FastAPI()

#CREATE
@app.post('/items', response_model=response_models.Item)
def createItem(item: response_models.ItemCreate, db: Session = Depends(getDb)):
    db_item = orm_models.Item(**item.model_dump())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

#READ
@app.get('/items/', response_model=list[response_models.Item])
def readItems(skip = 0, limit = 100 , db: Session = Depends(getDb)):
    items = db.query(orm_models.Item).offset(skip).limit(limit).all()
    return items

@app.get('/items/{item_id}', response_model=response_models.Item)
def readItem(item_id: int, db: Session = Depends(getDb)):
    db_item = db.query(orm_models.Item).filter(orm_models.Item.id == item_id).first()
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    
    return db_item

#UPDATE
@app.put('/items/{item_id}', response_model=response_models.Item)
def updateItem(item_id: int, item: response_models.Item, db: Session = Depends(getDb)):
    db_item = db.query(orm_models.Item).filter(orm_models.Item.id == item_id).first()

    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")

    for key, value in item.model_dump().items():
        setattr(db_item, key, value)

    db.commit()
    db.refresh(db_item)
    return db_item

#DELETE
@app.delete('/items/{item_id}')
def delete_item(item_id: int, db: Session = Depends(getDb)):
    db_item = db.query(orm_models.Item).filter(orm_models.Item.id == item_id).first()
    if db_item is None:
        raise HTTPException(status_code=404, detail="no found")
    
    db.delete(db_item)
    db.commit()
    return None