📝 Day 36 Notes
1. What is Backend?

The backend is responsible for:

Processing client requests
Applying business logic
Communicating with the database
Returning responses
2. Frontend vs Backend
Frontend	Backend
User Interface	Business Logic
HTML, CSS, JS	Python, Java, Node.js
Runs in Browser	Runs on Server
3. API

API (Application Programming Interface) is a bridge between the frontend and backend.

Example:

Browser
   │
   ▼
API
   │
   ▼
Backend
   │
   ▼
Database
4. REST API

REST APIs use HTTP methods to work with resources.

Method	Purpose
GET	Read data
POST	Create data
PUT	Update data
DELETE	Delete data
5. FastAPI

FastAPI is a modern Python framework used to build high-performance APIs.

Advantages
Very fast
Easy to learn
Automatic API documentation
Built-in data validation
Excellent support for Python type hints
6. Installing
pip install fastapi uvicorn
7. Creating an App
from fastapi import FastAPI

app = FastAPI()
8. Creating an Endpoint
@app.get("/")
def home():
    return {"message": "Hello, FastAPI!"}
@app.get("/") → Responds to GET requests at /.
9. Running the Server
uvicorn main:app --reload
main → Python file (main.py)
app → FastAPI application object
--reload → Automatically reloads when code changes
10. Swagger UI

Open:

http://127.0.0.1:8000/docs

Features:

Interactive documentation
Test endpoints
View request/response
See HTTP status codes

📚 Day 37 Notes
1. Path Parameters
Used to identify a specific resource.
Defined using {}.

Example:

@app.get("/student/{student_id}")
def get_student(student_id: int):
    return {"student_id": student_id}
2. Query Parameters
Used to filter, search, sort, or customize results.
Written after ?.

Example:

/students?branch=CSE
3. Combining Both

Example:

@app.get("/student/{student_id}")
def get_student(student_id: int, branch: str = "Smart Manufacturing"):
    return {
        "student_id": student_id,
        "branch": branch
    }
4. Default Values
branch: str = "Smart Manufacturing"

If the client doesn't provide branch, FastAPI uses the default value.

5. Automatic Validation
student_id: int

Valid:

/student/101

Invalid:

/student/abc

FastAPI automatically returns:

HTTP 422 Unprocessable Entity

No extra validation code is needed.

6. Testing APIs

You learned two methods:

Browser
http://127.0.0.1:8000/student/101
Swagger UI
http://127.0.0.1:8000/docs

Use Try it out → Execute to test endpoints interactively.

📝 Day 38 Notes
1. Request Body
Used to send data from the client to the server.
Most commonly sent as JSON.

Example:

{
  "name": "Surya",
  "age": 20,
  "branch": "Smart Manufacturing"
}
2. JSON
Stands for JavaScript Object Notation.
Used for exchanging data between applications.
Stores data as key-value pairs.

Rules:

Keys and strings use double quotes.
Numbers are not enclosed in quotes.
3. Pydantic Model
from pydantic import BaseModel

class Student(BaseModel):
    name: str
    age: int
    branch: str

A Pydantic model:

Defines the structure of incoming data.
Specifies the expected data types.
Automatically validates the request.
4. POST Endpoint
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Student(BaseModel):
    name: str
    age: int
    branch: str

@app.post("/student")
def create_student(student: Student):
    return {
        "message": "Student Created Successfully!",
        "student": student
    }
5. Accessing Data

Inside the endpoint:

student.name
student.age
student.branch

FastAPI converts the incoming JSON into a Student object automatically.

6. Automatic Validation

If:

age: int

and the client sends:

{
  "age": "twenty"
}

FastAPI automatically returns:

HTTP 422 – Unprocessable Entity

No manual validation code is required.

7. Testing with Swagger UI

Open:

http://127.0.0.1:8000/docs
Click POST /student
Click Try it out
Send JSON
Click Execute

Swagger UI makes testing APIs very easy during development.

students = []
Stored in RAM.
Data disappears when the server stops.
Good for learning, not suitable for production.
7. Why Databases?

Databases provide:

✅ Permanent storage
✅ Efficient searching and updating
✅ Structured organization of data
✅ Support for multiple users
✅ Better scalability and reliability