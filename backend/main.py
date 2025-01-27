from typing import List, Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Person(BaseModel):
    id: int
    name: str
    age: int
    
DB: List[Person] = [
    Person(id=1, name="Marvel", age= 29),
    Person(id=2, name="Teo", age = 29)

]

@app.get("/api")
def read_root():
    return DB


