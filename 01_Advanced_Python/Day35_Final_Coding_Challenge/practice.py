import json 
import logging
from pathlib import Path
from typing import List
from datetime import datetime

# Configure Logging
logging.basicConfig(
    filename="student.log",
    level=logging.INFO,
    format="%(asctime)s-%(levelname)s-%(message)s"
)

class Student:
    def __init__(self,name: str,age: int,branch: str):
        self.name = name
        self.age = age
        self.branch = branch
        self.created_at=datetime.now().strftime("%Y-%m-%d % H:%M:%S")

    def to_dict(self):
        return {
            "name": self.name,
            "age": self.age,
            "branch": self.branch,
            "created_at": self.created_at
        }

def save_students(students: List[Student], filename: str) -> None:
    data=[student.to_dict() for student in students]

    with open(filename, "w") as file:
        json.dump(data, file, indent=4)

    logging.info("Student data saved successfully.")


def load_students(filename: str):
    path = Path(filename)

    if not path.exists():
        print("File does not exist.")
        logging.warning("Tried to load a missing file.")
        return

    with open(filename, "r") as file:
        data = json.load(file)

    print("\nStudent Records")
    print("----------------------------")

    for student in data:
        print(f"Name   : {student['name']}")
        print(f"Age    : {student['age']}")
        print(f"Branch : {student['branch']}")
        print(f"Added  : {student['created_at']}")
        print()


try:
    students = [
        Student("Surya", 20, "Smart Manufacturing"),
        Student("Ravi", 21, "Computer Science"),
        Student("Ramesh", 22, "Mechanical")
    ]

    save_students(students, "students.json")
    load_students("students.json")

except Exception as e:
    logging.error(f"Error: {e}")
    print("Something went wrong.")