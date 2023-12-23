from fastapi import FastAPI, HTTPException
from typing import Optional, List
from pydantic import BaseModel


class Todo(BaseModel):
    name: str
    due_date: str
    desc: str


app = FastAPI(title="Todo api")

store = []


@app.get('/')
async def get_home():
    return {"hello": "world"}


@app.post('/todo/')
async def create_todo(todo: Todo):
    store.append(todo)
    return todo


@app.get('/todo/', response_model=List[Todo])
async def get_all_todos():
    return store


@app.get('/todo/{id}')
async def to_do(id: int):
    try:
        return store[id]
    except:
        raise HTTPException(status_code=404, detail="Todo not found")


@app.put('/todo/{id}')
async def update_todo(id: int, todo: Todo):
    try:
        store[id] = todo
        return store[id]
    except:
        raise HTTPException(status_code=404, detail="Todo not found")


@app.delete('/todo/{id}')
async def delete_todo(id :int):
    try:
        obj = store[id]
        store.pop(id)
        return obj
    except:
        raise HTTPException(status_code=404, detail="Todo not found")
