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

📝 Day 40 Notes
1. What is a Database?

A database stores data permanently on disk.

Example:

ID	Name	Age	Branch
1	Surya	20	Smart Manufacturing

Unlike a Python list, the data remains even after restarting the program.

2. SQLite

SQLite is:

✅ Built into Python (sqlite3)
✅ Lightweight
✅ File-based
✅ Great for learning and small to medium projects

Import it with:

import sqlite3
3. Connecting to a Database
conn = sqlite3.connect("students.db")

This creates (if needed) and connects to the database file.

4. Cursor
cursor = conn.cursor()

The cursor is used to execute SQL commands.

5. Creating a Table
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER,
    branch TEXT
)

Important keywords:

PRIMARY KEY → Unique identifier.
AUTOINCREMENT → IDs increase automatically.
TEXT → String values.
INTEGER → Numeric values.
6. Saving Changes
conn.commit()

Without commit(), changes may not be saved to the database.

7. Inserting Data
cursor.execute(
    """
    INSERT INTO students(name, age, branch)
    VALUES (?, ?, ?)
    """,
    ("Surya", 20, "Smart Manufacturing")
)

Using ? placeholders is the recommended and secure way to pass values.

8. Reading Data
cursor.execute("SELECT * FROM students")

rows = cursor.fetchall()

for row in rows:
    print(row)

fetchall() returns every row from the query result.


📝 Day 41 Notes
1. Connect FastAPI to SQLite
conn = sqlite3.connect(
    "students.db",
    check_same_thread=False
)

cursor = conn.cursor()
2. Create
INSERT INTO students(name, age, branch)
VALUES (?, ?, ?)
3. Read
SELECT * FROM students

and:

rows = cursor.fetchall()
4. Update
UPDATE students
SET name = ?, age = ?, branch = ?
WHERE id = ?
5. Delete
DELETE FROM students
WHERE id = ?
6. Save Changes

For operations that modify the database:

conn.commit()

Remember:

SELECT → read
INSERT → create
UPDATE → modify
DELETE → remove

📝 Day 42 Notes
1. Separation of Concerns

Different parts of the application should have different responsibilities.

main.py       → API
database.py   → Database
models.py     → Data validation
2. Modular Programming

Instead of:

main.py
 ├── Database
 ├── Models
 ├── API
 ├── CRUD
 └── Everything else

we divide it into modules:

main.py
database.py
models.py
Benefits
Easier maintenance
Easier debugging
Easier modifications
Better readability
Code can be reused
3. database.py

Contains database-related code:

import sqlite3

conn = sqlite3.connect(
    "students.db",
    check_same_thread=False
)

cursor = conn.cursor()
4. models.py

Contains Pydantic models:

from pydantic import BaseModel

class Student(BaseModel):
    name: str
    age: int
    branch: str
5. main.py

Contains the API endpoints:

from fastapi import FastAPI
from database import cursor, conn
from models import Student

Then:

POST
GET
PUT
DELETE

📝 Day 43 Notes
1. ORM

ORM = Object-Relational Mapping

It allows us to work with database tables using Python objects/classes.

Database Table ↔ Python Class
Database Row   ↔ Python Object
2. SQLAlchemy

SQLAlchemy is the ORM we used.

from sqlalchemy import create_engine

It connects our Python application to the database.

3. SQLAlchemy Model
class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    branch = Column(String)

This represents the students database table.

4. Session
db = SessionLocal()

The session is used to perform database operations.

Create
db.add(student)
db.commit()
Read
students = db.query(Student).all()
Update
student.name = "Rahul"
db.commit()
Delete
db.delete(student)
db.commit()
🔥 Most Important Comparison
Before — Raw SQLite
cursor.execute("""
INSERT INTO students(...)
VALUES (...)
""")
Now — SQLAlchemy
student = Student(...)
db.add(student)
db.commit()

SQLAlchemy handles the underlying SQL for us.

📝 Day 44 Notes
1. Dependency Injection

FastAPI can automatically provide things an endpoint needs.

db: Session = Depends(get_db)
2. Database Dependency
def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()

Flow:

Request
 ↓
get_db()
 ↓
Create Session
 ↓
yield db
 ↓
Endpoint
 ↓
finally
 ↓
Close Session
3. Pydantic vs SQLAlchemy

This is very important:

Pydantic
   ↓
API input/output validation

SQLAlchemy
   ↓
Database representation & operations

Example:

class StudentRequest(BaseModel):
    name: str
    age: int
    branch: str

vs.

class Student(Base):
    __tablename__ = "students"
4. CRUD with Dependencies

You now have:

POST   /student
GET    /students
PUT    /student/{student_id}
DELETE /student/{student_id}

And each database endpoint can use:

db: Session = Depends(get_db)
5. db.refresh()

After creating:

db.add(new_student)
db.commit()
db.refresh(new_student)

refresh() gets the latest database state back into the Python object, including generated values such as the ID.

📚 Day 45 Notes — Clean FastAPI Project Structure
1. Why we separate files

Putting everything inside main.py works for small projects, but as the project grows it becomes difficult to:

Find code
Modify code
Debug problems
Maintain the project
Work with multiple developers

The solution is Separation of Concerns.

Each file gets a specific responsibility.

2. Day 45 Project Structure

Our project now looks like:

Day45_Clean_FastAPI/
│
├── main.py
├── database.py
├── models.py
├── schemas.py
│
└── routers/
    └── students.py
Responsibility of each file
File	Purpose
main.py	FastAPI application setup
database.py	Database connection and sessions
models.py	SQLAlchemy database models
schemas.py	Pydantic validation models
routers/students.py	Student API endpoints
3. database.py

Contains database configuration.

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./students.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

It also contains our dependency:

def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()
Remember
database.py
     ↓
Database connection
     ↓
SessionLocal
     ↓
get_db()
4. models.py

Contains SQLAlchemy models.

Example:

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    age = Column(Integer)
    branch = Column(String)

This represents the database table.

Think:

SQLAlchemy Model
       ↓
Database Table
5. schemas.py

Contains Pydantic models.

from pydantic import BaseModel

class StudentRequest(BaseModel):
    name: str
    age: int
    branch: str

This handles API data validation.

For example:

{
    "name": "Surya",
    "age": 20,
    "branch": "Smart Manufacturing"
}

FastAPI checks:

name   → str
age    → int
branch → str
6. SQLAlchemy vs Pydantic

This distinction is very important.

SQLAlchemy
models.py
     ↓
Database representation
     ↓
CRUD operations
Pydantic
schemas.py
     ↓
API input/output
     ↓
Validation

So:

SQLAlchemy talks to the database.
Pydantic validates API data.

7. APIRouter

Instead of putting all endpoints in main.py, we use:

from fastapi import APIRouter

router = APIRouter(
    prefix="/students",
    tags=["Students"]
)

Then:

@router.get("/")

becomes:

GET /students/

And:

@router.post("/")

becomes:

POST /students/

because of:

prefix="/students"
8. Why APIRouter?

Suppose your application eventually has:

Students
Products
Orders
Users
Payments
Authentication

Instead of:

main.py
 ├── 500 endpoints 😵

we can have:

routers/
├── students.py
├── products.py
├── orders.py
├── users.py
└── authentication.py

Much easier to manage.

9. include_router()

In main.py:

from fastapi import FastAPI
from routers.students import router as student_router

app = FastAPI()

app.include_router(student_router)

This connects the student router to the main FastAPI application.

Think:

students.py
     ↓
student_router
     ↓
include_router()
     ↓
FastAPI app
10. tags

We used:

router = APIRouter(
    prefix="/students",
    tags=["Students"]
)

tags organizes endpoints in Swagger.

You'll see:

Students

GET    /students/
POST   /students/
PUT    /students/{student_id}
DELETE /students/{student_id}
11. Complete Architecture

Your Day 45 backend now follows:

                   FastAPI
                      │
                   main.py
                      │
                include_router()
                      │
                students.py
                      │
             ┌────────┴────────┐
             ↓                 ↓
         schemas.py       database.py
             ↓                 ↓
          Pydantic          SQLAlchemy
                               ↓
                           models.py
                               ↓
                            SQLite
⭐ Most Important Things to Remember
1.
main.py
→ Application
2.
database.py
→ Database connection/session
3.
models.py
→ SQLAlchemy/database tables
4.
schemas.py
→ Pydantic/API validation
5.
routers/
→ API endpoints
6.
Depends(get_db)

→ FastAPI automatically provides the database session.

7.
APIRouter()

→ Organizes related endpoints.

8.
app.include_router()

→ Connects a router to the FastAPI application.

📚 Day 46 Notes — Request & Response Schemas
1. Why separate request and response schemas?

A real API should control:

What the client is allowed to send
What the API returns

Instead of using one schema for everything, we created separate schemas.

Client
  ↓
Request Schema
  ↓
Backend
  ↓
Database
  ↓
Response Schema
  ↓
Client
2. StudentCreate

In schemas.py:

from pydantic import BaseModel


class StudentCreate(BaseModel):
    name: str
    age: int
    branch: str

This represents input coming from the client.

Example:

{
    "name": "Rahul",
    "age": 21,
    "branch": "CSE"
}

Notice there is no id.

Why?

Because the database generates the ID.

3. StudentResponse
class StudentResponse(BaseModel):
    id: int
    name: str
    age: int
    branch: str

    model_config = {
        "from_attributes": True
    }

This represents data going back to the client.

Example:

{
    "id": 5,
    "name": "Rahul",
    "age": 21,
    "branch": "CSE"
}
4. response_model

We can tell FastAPI exactly what the endpoint should return:

@router.post("/", response_model=StudentResponse)

This means:

The response should follow the StudentResponse structure.

FastAPI/Pydantic handles the response serialization instead of us manually creating dictionaries.

5. List Response

For multiple students:

@router.get("/", response_model=list[StudentResponse])

This means:

Response
   ↓
List
   ↓
StudentResponse
StudentResponse
StudentResponse
...

Example:

[
    {
        "id": 1,
        "name": "Rahul",
        "age": 21,
        "branch": "CSE"
    },
    {
        "id": 2,
        "name": "Aman",
        "age": 22,
        "branch": "SM"
    }
]
6. from_attributes=True

We return a SQLAlchemy object:

return new_student

But new_student is a SQLAlchemy object, not a dictionary.

This configuration:

model_config = {
    "from_attributes": True
}

allows Pydantic to read attributes such as:

new_student.id
new_student.name
new_student.age
new_student.branch

and create the StudentResponse.

7. Request vs Response

This is one of today's most important concepts:

Schema	Direction	Purpose
StudentCreate	Client → API	Validate input
StudentResponse	API → Client	Structure output

Remember:

Create = INPUT
Response = OUTPUT

8. HTTPException

When a student doesn't exist:

if existing_student is None:
    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )

The API returns:

{
    "detail": "Student not found"
}

with:

HTTP 404 Not Found
Why?

Because the requested resource doesn't exist.

9. Why not return a normal dictionary?

Previously we might write:

return {
    "id": new_student.id,
    "name": new_student.name,
    "age": new_student.age,
    "branch": new_student.branch
}

Now we can simply write:

return new_student

because:

response_model=StudentResponse

controls the response.

This makes our code cleaner and easier to maintain.

10. Complete Architecture

Your Day 46 API now follows:

                    Client
                      │
                      ↓
               StudentCreate
                      │
                 Validation
                      │
                      ↓
                 FastAPI Router
                      │
                      ↓
                  SQLAlchemy
                      │
                      ↓
                   SQLite
                      │
                      ↓
              StudentResponse
                      │
                 Serialization
                      │
                      ↓
                    Client
⭐ Key Code to Remember
Request schema
class StudentCreate(BaseModel):
    name: str
    age: int
    branch: str
Response schema
class StudentResponse(BaseModel):
    id: int
    name: str
    age: int
    branch: str

    model_config = {
        "from_attributes": True
    }
Response model
@router.get("/", response_model=list[StudentResponse])
Single response
@router.post("/", response_model=StudentResponse)
HTTP error
raise HTTPException(
    status_code=404,
    detail="Student not found"
)



