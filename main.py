'''
Minimal example using fastAPI.
'''
from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel


class Employee(BaseModel):
    first_name: str
    last_name: str
    company: str
    age: int
    phone: Optional[str] = None


app = FastAPI()


@app.get("/")
def hello():
    return {"Hello": "API"}


@app.post("/create_employee/")
def create_employee(employee: Employee):
    return {
        "status": "created",
        "data": employee
    }
