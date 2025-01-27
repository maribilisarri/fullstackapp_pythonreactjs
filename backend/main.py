from typing import List, Optional
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Replace with your React app's URL
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

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


