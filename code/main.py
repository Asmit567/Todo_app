from model import Todo, TodoTable
from fastapi import FastAPI, Query
from typing import List  
from starlette.middleware.cors import CORSMiddleware  
from db import session  

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/items")
def read_items():
    items = session.query(TodoTable).all()
    return items


@app.get("/items/{item_id}")
def read_item(item_id: int):
    item = session.query(TodoTable).\
        filter(TodoTable.id == item_id).first()
    return item


@app.post("/item")
async def create_item(title: str, status: str = Query("New", enum=["New", "Started", "Pending", "Closed", "Finished"])):
    item = TodoTable()
    item.title = title
    item.status = status
    session.add(item)
    session.commit()
    return item


@app.put("/items")
async def update_items(items: List[Todo]):
    for new_item in items:
        item = session.query(TodoTable).\
            filter(TodoTable.id == new_item.id).first()
        item.title = new_item.title
        item.status = new_item.status
        session.commit()
    return items


@app.post("/fetch_status")
def fetch_status(status: str = Query("New", enum=["New", "Started", "Pending", "Closed", "Finished"])):
    items = session.query(TodoTable).\
        filter(TodoTable.status== status).all()
    return items
