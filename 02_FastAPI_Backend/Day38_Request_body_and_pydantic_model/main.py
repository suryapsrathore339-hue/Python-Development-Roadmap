from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()

class Student(BaseModel):
    name:str
    age:int
    branch:str

@app.post("/student")
def create_student(student:Student):
    return{
        "message":"Student created successfully",
        "student":student
    }