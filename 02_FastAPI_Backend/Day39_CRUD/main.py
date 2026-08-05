from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()

class Student(BaseModel):
    name:str
    age:int
    branch:str

students=[]

@app.post("/student")
def create_student(student:Student):
    students.append(student)
    return {
        "message":"Student Added Successfully",
        "student":student
    }

@app.get("/student")
def get_students():
    return students

@app.put("/student/{student_id}")
def update_student(student_id:int, student:Student):
    return {
        "message":"Student Updated Sucessfully",
        "student_id":student_id,
        "student":student
    }

@app.delete("/student/{student_id}")
def delete_student(student_id:int):
    return {
        "message":"Student Deleted Successfully",
        "student_id":student_id
    }

