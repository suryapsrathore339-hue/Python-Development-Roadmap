from fastapi import FastAPI

app=FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to the FastAPI"}

@app.get("/student/{student_id}")
def get_student(student_id: int,branch: str="Smart Manufacturing"):
    return {
        "student_id": student_id,
        "branch": branch
    }