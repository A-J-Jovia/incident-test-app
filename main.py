from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float

@app.get('/')
def read_root():
    return {'Hello': 'World'}

@app.post('/items/')
def create_item(item: Item):
    return item

def add(a: int, b: int):
    return a + b

x = add(1, 2) # corrected type error

def do_something():
    pass

do_something() # fixed function name typo