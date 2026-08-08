from fastapi import FastAPI
from database import cursor, conn
from models import Student

app=FastAPI()

@app.get("/student")
def create_student(student: Student):

    cursor.execute(
        """
        INSERT INTO students(name,age,branch)
        VALUES(?,?,?)
        """,
        (student.name, student.age, student.branch)
    )
    conn.commit()

    return {
        "message": "Student created successfully"
    }

@app.get("/students")
def get_students():

    cursor.execute("SELECT * FROM students")
    rows=cursor.fetchall()
    return rows


@app.put("/student/{student_id}")
def update_student(student_id: int, student: Student):

    cursor.execute(
        """
        UPDATE students
        SET name = ?, age = ?, branch = ?
        WHERE id = ?
        """,
        (student.name, student.age, student.branch, student_id)
    )

    conn.commit()

    return {
        "message": "Student Updated Successfully"
    }

@app.delete("/student/{student_id}")
def delete_student(student_id: int):

    cursor.execute(
        "DELETE FROM students WHERE id = ?",
        (student_id,)
    )

    conn.commit()

    return {
        "message": "Student Deleted Successfully"
    }