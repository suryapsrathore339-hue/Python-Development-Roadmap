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

📚 Day 48 Notes — Path Parameters, Query Parameters & Filtering

Today we made your FastAPI backend more flexible by allowing the client to specify which data it wants.

1. Path Parameters

A path parameter is part of the URL path and is generally used to identify a specific resource.

Example:

/students/15

Here:

15 → student_id

FastAPI:

@router.get("/{student_id}", response_model=StudentResponse)
def get_student(
    student_id: int,
    db: Session = Depends(get_db)
):

Because we wrote:

student_id: int

FastAPI expects the path parameter to be an integer.

Example
GET /students/5

means:

Get the student whose ID is 5.

2. Query Parameters

Query parameters appear after ?.

Example:

/students/?branch=SM

Here:

branch=SM

is a query parameter.

FastAPI:

branch: str | None = None

means:

branch is an optional query parameter.

3. Path vs Query Parameter
Path
/students/5

Used to identify a specific student.

Query
/students/?branch=SM

Used to filter/customize a collection.

Remember:
Path  → Which specific resource?
Query → How should I filter/customize the collection?
4. Get One Student

We created:

@router.get("/{student_id}", response_model=StudentResponse)
def get_student(
    student_id: int,
    db: Session = Depends(get_db)
):
    student = db.query(Student).filter(
        Student.id == student_id
    ).first()


    if student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )


    return student
Flow
GET /students/5
       ↓
student_id = 5
       ↓
SQLAlchemy searches database
       ↓
Student found?
   ↙         ↘
 Yes          No
 ↓             ↓
Student      404
 ↓
200
5. Optional Query Parameter

We used:

branch: str | None = None

This means the parameter is optional.

Without branch:
GET /students/

→ Return all students.

With branch:
GET /students/?branch=SM

→ Return only SM students.

6. Filtering with SQLAlchemy

We started with:

query = db.query(Student)

Then:

if branch is not None:
    query = query.filter(Student.branch == branch)

Finally:

return query.all()

So:

Database
   ↓
SQLAlchemy Query
   ↓
Apply filters
   ↓
Return matching records
7. Multiple Filters

We added:

age: int | None = None

and:

if age is not None:
    query = query.filter(Student.age == age)

Now:

GET /students/?branch=SM&age=20

applies both filters.

Meaning:

Return students whose branch is SM AND whose age is 20.

8. Name Filtering

We also added:

name: str | None = None

and:

if name is not None:
    query = query.filter(Student.name == name)

So we can use:

GET /students/?name=Surya

or combine:

GET /students/?name=Surya&branch=SM
9. Final GET Endpoint

Your endpoint should now look like:

@router.get("/", response_model=list[StudentResponse])
def get_students(
    branch: str | None = None,
    age: int | None = None,
    name: str | None = None,
    db: Session = Depends(get_db)
):
    query = db.query(Student)


    if branch is not None:
        query = query.filter(Student.branch == branch)


    if age is not None:
        query = query.filter(Student.age == age)


    if name is not None:
        query = query.filter(Student.name == name)


    return query.all()

This is a clean basic filtering implementation.

10. Empty Results vs 404

This was the most important distinction from today's quiz.

Specific resource doesn't exist:
GET /students/999

→

404 Not Found

because we're asking for one specific student.

Filter finds nothing:
GET /students/?branch=ABC

→

[]

with:

200 OK

because the request itself is valid; there simply aren't any matching students.

Remember:
Specific resource missing → 404


Valid collection filter with zero matches → 200 + []
11. Query Parameters Can Be Combined

Example:

/students/?branch=SM&age=20&name=Surya

Contains three query parameters:

branch = SM
age    = 20
name   = Surya

The database query applies all three filters.

12. Why Filter in the Database?

Instead of:

students = db.query(Student).all()


for student in students:
    # filter manually

we use:

query = query.filter(Student.branch == branch)

This is better because the database does the filtering.

Benefits:

Less unnecessary data transferred
Cleaner code
More efficient for larger datasets
Database engines are designed for filtering/searching
🧠 Day 48 Cheat Sheet
PATH PARAMETERS
/students/5
        ↓
student_id = 5
        ↓
Specific resource
QUERY PARAMETERS
/students/?branch=SM
             ↓
          branch=SM
             ↓
          Filtering
MULTIPLE QUERY PARAMETERS
/students/?branch=SM&age=20
             ↓
       Branch AND Age
Status behavior
GET /students/999
→ 404 if student doesn't exist


GET /students/?branch=ABC
→ 200 + [] if no match

📚 Day 49 Notes — Pagination & Sorting in FastAPI

Today we upgraded your FastAPI student API to handle large datasets efficiently.

Previously:

db.query(Student).all()

could return every student at once.

Today we learned how to control how many records are returned, where to start, and how they are ordered.

1. Pagination

Pagination means dividing a large result set into smaller portions.

For example, if we have 100 students and want 10 per page:

Page 1 → 1–10
Page 2 → 11–20
Page 3 → 21–30
...

Instead of returning all 100 students at once.

2. skip

skip tells the database how many records to skip.

/students/?skip=10

means:

Skip the first 10 matching records.

Examples:

skip=0 → start from beginning
skip=10 → skip first 10
skip=20 → skip first 20
3. limit

limit tells the API the maximum number of records to return.

/students/?limit=5

means:

Return at most 5 students.

Remember:

limit=5

means maximum 5, not minimum 5.

4. offset() and limit() in SQLAlchemy

We used:

query.offset(skip).limit(limit).all()

For example:

db.query(Student).offset(10).limit(5).all()

means:

Skip first 10
      ↓
Return next 5 at most
5. Why Pagination Matters

This:

db.query(Student).all()

can become problematic when there are millions of records.

It may:

Retrieve huge amounts of data
Consume more memory
Increase database workload
Increase network transfer
Make API responses slower

Pagination lets us request only what we need.

6. Sorting

We also added sorting.

Example:

/students/?sort_by=age

means:

Sort students by age.

SQLAlchemy:

query.order_by(Student.age)

By default, this gives ascending order.

Example:

18
19
20
21
22
7. Descending Sorting

For descending order:

Student.age.desc()

Example:

/students/?sort_by=age&order=desc

Result:

22
21
20
19
18
8. Ascending vs Descending
Student.age.asc()

→ Smallest to largest

Student.age.desc()

→ Largest to smallest

9. Controlled Sorting Fields

We used:

if sort_by == "name":
    column = Student.name
elif sort_by == "age":
    column = Student.age
else:
    column = Student.id

This is important because we don't blindly accept arbitrary user input as a database column.

We explicitly control the allowed fields:

name → Student.name
age  → Student.age
id   → Student.id

This makes the API predictable and safer.

10. Complete GET Endpoint

Your current endpoint should look like:

@router.get("/", response_model=list[StudentResponse])
def get_students(
    branch: str | None = None,
    age: int | None = None,
    name: str | None = None,
    skip: int = 0,
    limit: int = 10,
    sort_by: str = "id",
    order: str = "asc",
    db: Session = Depends(get_db)
):
    query = db.query(Student)


    # Filtering
    if branch is not None:
        query = query.filter(Student.branch == branch)


    if age is not None:
        query = query.filter(Student.age == age)


    if name is not None:
        query = query.filter(Student.name == name)


    # Sorting
    if sort_by == "name":
        column = Student.name
    elif sort_by == "age":
        column = Student.age
    else:
        column = Student.id


    if order == "desc":
        query = query.order_by(column.desc())
    else:
        query = query.order_by(column.asc())


    # Pagination
    return query.offset(skip).limit(limit).all()
11. Complete Request Flow

A request such as:

/students/?branch=SM&sort_by=age&order=desc&skip=0&limit=3

is processed conceptually as:

              Request
                 ↓
        branch = SM
                 ↓
          Filter database
                 ↓
        sort_by = age
                 ↓
       Sort by age
                 ↓
        order = desc
                 ↓
       Highest → lowest
                 ↓
          skip = 0
                 ↓
        limit = 3
                 ↓
      Return up to 3
12. Combining Everything

Your API now supports:

All students
GET /students/
Specific student
GET /students/5
Filtering
GET /students/?branch=SM
Multiple filters
GET /students/?branch=SM&age=20
Pagination
GET /students/?skip=10&limit=5
Sorting
GET /students/?sort_by=age&order=desc
Everything together
GET /students/?branch=SM&sort_by=age&order=desc&skip=0&limit=3

Meaning:

Find SM students → sort them by age descending → skip none → return at most 3.

📝 Day 50 Notes
Dependencies

A dependency is a reusable component that FastAPI automatically provides to an endpoint.

Syntax:

value = Depends(function)

Example:

db: Session = Depends(get_db)
Dependency Injection

Instead of an endpoint creating everything itself:

Endpoint → create dependency

FastAPI handles it:

FastAPI → Dependency → Endpoint
Service Layer

Services contain application/business logic.

Router
  ↓
Service
  ↓
Database

Router should primarily handle HTTP concerns.

Service handles operations such as:

create
read
update
delete
Reusability

Instead of repeating logic:

student = db.query(Student)...

create reusable components.

You implemented this through:

get_student()

and:

student_service.*
⭐ Day 50 Score
Area	Score
Dependencies	9/10
Dependency Injection	9/10
Reusability	8.5/10
Service Layer	8.5/10
Practical implementation	10/10
Understanding	8.5/10
🏆 Overall: 9/10

The only thing to improve is being more precise about where different responsibilities belong. You initially placed the service logic conceptually in main.py, but you corrected that quickly.

📊 Roadmap Progress
Days completed: 50 / 90
Progress: 55.6%

Python:        Days 1–35 ✅
FastAPI:       Days 36–50 ✅
FastAPI left:  Days 51–65
Advanced ML:   Days 66–90

And importantly, you're now moving from:

"I know FastAPI"

toward:

"I understand how to structure a backend application."

That's much more valuable for your GSoC 2027 open-source objective.


📝 Day 51 Notes
1. Python Packages

A folder containing __init__.py can act as a Python package:

models/
├── __init__.py
└── student.py

__init__.py can expose objects:

from .student import Student

allowing:

from models import Student
2. Models vs Schemas

This distinction is very important.

Model:

How is data stored?

Example:

class Student(Base):
    ...

Schema:

What data does the API accept/return?

Example:

class StudentCreate(BaseModel):
    ...
3. Router

Handles HTTP:

GET
POST
PUT
DELETE

and delegates actual work.

4. Service

Handles operations:

create_student()
get_students()
update_student()
delete_student()
5. Dependency

Reusable functionality:

get_student()

which is used by:

PUT
DELETE

📝 Day 52 Notes
1. Environment Variables

Used to keep configuration outside source code.

DATABASE_URL=sqlite:///./students.db

Instead of:

DATABASE_URL = "sqlite:///./students.db"
2. .env

Contains your local configuration:

DATABASE_URL=sqlite:///./students.db
APP_NAME=Student Management API

Should not be committed when it contains secrets.

3. .env.example

Provides a template for other developers:

DATABASE_URL=
APP_NAME=Student Management API

This can safely be committed.

4. Pydantic Settings

You created:

config/
└── settings.py

with:

class Settings(BaseSettings):
    DATABASE_URL: str
    APP_NAME: str

This provides:

configuration centralization
type validation
environment variable loading
cleaner application architecture
5. settings

You can now access configuration through:

from config.settings import settings

and:

settings.DATABASE_URL
settings.APP_NAME

📚 Day 53 Notes — Authentication Fundamentals

Status: 🟢 Day 53 Partially Complete
Time: ~1 hour
Progress: ~75%

1. Authentication vs Authorization
Authentication

Answers:

Who are you?

Example:

username + password
        ↓
   Authentication
        ↓
   User verified
Authorization

Answers:

What are you allowed to do?

Example:

Authenticated user
        ↓
Is user an admin?
        ↓
Can DELETE students?

Remember:

Authentication → Who are you?
Authorization  → What can you do?
2. Never Store Plain-Text Passwords

❌ Bad:

password = "surya123"

stored directly in the database.

If the database is compromised, the passwords are immediately exposed.

Correct approach
Password
   ↓
Hash
   ↓
Password Hash
   ↓
Database

Your database stores:

$argon2id$...

instead of:

surya123
3. Hashing vs Encryption
Encryption
Plain text
    ↓
Encryption
    ↓
Encrypted data
    ↓
Can be decrypted
Password hashing
Password
    ↓
Hashing
    ↓
Hash

Password hashing is designed to be one-way.

We don't decrypt the hash during login.

4. pwdlib

You installed:

python -m pip install "pwdlib[argon2]"

We created:

utils/
└── security.py
security.py
from pwdlib import PasswordHash


password_hash = PasswordHash.recommended()


def hash_password(password: str) -> str:
    return password_hash.hash(password)


def verify_password(
    plain_password: str,
    hashed_password: str
) -> bool:
    return password_hash.verify(
        plain_password,
        hashed_password
    )
5. Password Hashing Flow

Registration:

"surya123"
     ↓
hash_password()
     ↓
$argon2id$...
     ↓
Database

Login:

"surya123"
     ↓
verify_password()
     ↓
stored hash
     ↓
True / False

We don't compare the plain password directly with the hash.

6. Salt

Two users can have the same password but different hashes.

For example:

User A → "password123" → hash A
User B → "password123" → hash B

The hashes don't necessarily match because password hashing uses a random salt.

pwdlib handles this for us.

7. User Model

We created:

models/
├── __init__.py
├── student.py
└── user.py

Our User model contains:

id
username
email
hashed_password

Important:

❌ password
✅ hashed_password
8. User Schemas

We created:

schemas/
├── student.py
├── user.py
└── auth.py
UserCreate

Used during registration:

{
    "username": "surya",
    "email": "surya@example.com",
    "password": "surya123"
}
UserResponse

Used when returning user information:

{
    "id": 1,
    "username": "surya",
    "email": "surya@example.com"
}

Notice that neither:

password

nor:

hashed_password

is returned.

9. Service Layer

We created:

services/
├── student_service.py
└── user_service.py

The user service handles:

Create user
    ↓
Check duplicate username/email
    ↓
Hash password
    ↓
Create User model
    ↓
Commit to database

This keeps business logic out of the router.

10. Registration Endpoint

We created:

POST /auth/register

Architecture:

Client
   ↓
UserCreate
   ↓
Auth Router
   ↓
User Service
   ↓
hash_password()
   ↓
User Model
   ↓
Database

Successful registration:

201 Created

Duplicate username/email:

400 Bad Request
11. Current Project Architecture

Your project is becoming much more professional:

Student Management API
│
├── config/
│   └── settings.py
│
├── models/
│   ├── __init__.py
│   ├── student.py
│   └── user.py
│
├── schemas/
│   ├── __init__.py
│   ├── student.py
│   ├── user.py
│   └── auth.py        ← started today
│
├── routers/
│   ├── students.py
│   └── auth.py
│
├── services/
│   ├── student_service.py
│   └── user_service.py
│
├── utils/
│   └── security.py
│
├── database.py
├── main.py
├── .env
├── .env.example
└── .gitignore

This is exactly the kind of modular structure we're aiming for before moving toward more advanced FastAPI/backend concepts.

📘 Day 54 — Notes
Today's objective

Understand and implement JWT-based authentication.

What you completed

1. Login service

Implemented:

authenticate_user()

Flow:

Username
   ↓
Find user
   ↓
Verify password hash
   ↓
Valid → User
Invalid → None

2. Login endpoint

Implemented:

POST /auth/login

Invalid credentials:

401 Unauthorized

3. JWT fundamentals

Learned:

JWT
├── Header
├── Payload
└── Signature

Important:

JWT is normally signed, not encrypted.

4. JWT configuration

Added:

JWT_SECRET_KEY

to .env and settings.

5. PyJWT

Installed:

python -m pip install PyJWT

6. Token utility

Created:

utils/token.py

with:

HS256
30-minute expiration
sub claim
exp claim

7. Successful login now returns

{
    "access_token": "eyJ...",
    "token_type": "bearer"
}

And you successfully tested:

Correct credentials → 200 + JWT ✅
Wrong credentials → 401 ✅
🧠 Architecture now

Your backend has evolved significantly:

                 AUTHENTICATION
                       │
          ┌────────────┴────────────┐
          ↓                         ↓
     REGISTER                      LOGIN
          │                         │
     Hash password            Verify password
          │                         │
          └────────────┬────────────┘
                       ↓
                  Generate JWT
                       ↓
                    Client

📘 Day 55 Notes — JWT & Protected Routes
1. OAuth2 Bearer Token

We introduced:

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/auth/login"
)

It extracts:

Authorization: Bearer <JWT>

from incoming requests.

2. JWT Verification

Created:

get_current_user()

The flow is:

Request
   ↓
Extract Bearer token
   ↓
jwt.decode()
   ↓
Verify signature
   ↓
Check expiration
   ↓
Read "sub"
   ↓
Return username

Invalid/expired token:

401 Unauthorized
3. FastAPI Security Dependency

We used:

username: str = Depends(get_current_user)

This is important because authentication logic is now reusable.

Any protected endpoint can use the same dependency.

4. Protected /auth/me

We created:

GET /auth/me

Without JWT:

401 Unauthorized ❌

With valid JWT:

{
    "message": "You are authenticated",
    "username": "surya"
}
5. Protected Student API

We applied the authentication dependency to:

GET /students/

Now:

No JWT → 401 ❌
Valid JWT → 200 ✅

Your existing filtering, pagination, and sorting still work after authentication.

🔑 Most important distinction
Authentication
"Who are you?"
       ↓
Valid JWT
Authorization
"What are you allowed to do?"
       ↓
Role / permissions

A valid JWT does not mean the user is an admin.

🏗️ Current architecture
Client
  ↓
POST /auth/login
  ↓
Verify password
  ↓
Generate JWT
  ↓
Client receives token
  ↓
Authorization: Bearer JWT
  ↓
get_current_user()
  ↓
Verify JWT
  ↓
Protected endpoint

from models import User


@router.get("/me")
def get_me(
    current_user: User = Depends(get_current_user)
):
    return {
        "message": "You are authenticated",
        "username": current_user.username,
        "email": current_user.email
    }


📘 Day 57 Notes — Authorization & Roles
🎯 Main Goal

Day 56 handled authentication — identifying the user.

Day 57 introduced authorization — deciding what that user is allowed to do.

Authentication → Who are you?
Authorization  → What can you do?
1. User Roles

We added a role field to the User model:

role = Column(
    String,
    default="student",
    nullable=False
)

Our initial roles are:

student
admin

So the User model conceptually becomes:

User
├── id
├── username
├── email
├── hashed_password
└── role
2. Default Role

New users should automatically become:

student

We do not allow the client to choose their own role during registration.

Bad:

role=user.role

A malicious client could send:

{
    "username": "hacker",
    "password": "123",
    "role": "admin"
}

and potentially give themselves admin privileges.

Security principle

Never trust the client with privilege assignment.

3. require_admin() Dependency

We created:

def require_admin(
    current_user: User = Depends(get_current_user)
):
    if current_user.role != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Admin access required"
        )

    return current_user

This dependency checks the authenticated user's role.

4. Authorization Flow
Request
   ↓
require_admin()
   ↓
get_current_user()
   ↓
Verify JWT
   ↓
Find User
   ↓
Check role
   ↓
┌───────────────┐
│ role = admin? │
└───────┬───────┘
    Yes │ No
        │
        ↓
     Continue
        │
        └──────→ 403 Forbidden
5. Protecting an Endpoint

For the DELETE student endpoint:

current_user: User = Depends(require_admin)

This means only authenticated administrators can execute the endpoint.

The endpoint itself doesn't need to contain:

if current_user.role != "admin":

The authorization dependency handles it.

6. Authentication vs Authorization

This is one of the most important concepts.

Authentication
Who are you?
       ↓
JWT
       ↓
User
Authorization
What can you do?
       ↓
User role
       ↓
Permissions

Example:

Valid JWT
   ↓
User = Surya
   ↓
role = student
   ↓
DELETE student
   ↓
403 Forbidden
7. 401 vs 403
401 Unauthorized

The request is not properly authenticated.

Examples:

No JWT
Invalid JWT
Expired JWT

Meaning:

"I don't know who you are."

403 Forbidden

The user is authenticated but doesn't have permission.

Example:

Valid JWT
   ↓
User identified
   ↓
role = student
   ↓
Admin endpoint

Meaning:

"I know who you are, but you're not allowed to do this."

8. Reusable Dependencies

The major architectural advantage is reusability.

Instead of writing authorization logic separately in every endpoint:

if current_user.role != "admin":
    ...

we can simply use:

Depends(require_admin)

on multiple endpoints.

DELETE /students/{id} ──┐
                        │
POST /students/ ────────┼──→ require_admin()
                        │
PUT /students/{id} ────┘
⚠️ SQLite Note

We added a new column:

role

but your existing students.db was created before this column existed.

Base.metadata.create_all() does not automatically modify an existing table's structure.

The proper production solution is database migrations, which we'll cover later.

Don't randomly delete your database just to fix schema changes.

🧠 Day 57 Key Takeaways
Authentication identifies the user.
Authorization determines permissions.
Users can have roles such as student and admin.
New users should default to the least-privileged role.
Never let users assign themselves privileged roles.
require_admin() is a reusable authorization dependency.
401 means authentication failed/missing.
403 means authentication succeeded but permission was denied.
FastAPI dependencies keep authorization logic clean and reusable.
Database schema changes should eventually be handled with migrations.

📚 Day 58 — RBAC Notes
1. What is RBAC?

RBAC = Role-Based Access Control

Instead of giving permissions individually to every user, we assign a role, and the role determines what the user can access.

Example:

Admin   → Delete students, manage users
Teacher → View/update students
Student → View limited information
2. Authentication vs Authorization
Concept	Question	Example
Authentication	Who are you?	Is this JWT valid?
Authorization	What can you do?	Is this user an admin?

Typical flow:

Request
   ↓
JWT Authentication
   ↓
Current User
   ↓
User's Role
   ↓
Permission Check
   ↓
Endpoint
3. 401 vs 403

This is very important.

401 Unauthorized → Authentication failed.

Examples:

No token
Invalid token
Expired token

403 Forbidden → User is authenticated but doesn't have permission.

Example:

student → tries admin endpoint
                ↓
              403
4. require_role()

Instead of writing separate functions like require_admin(), we created a reusable dependency:

def require_role(required_role: str):

    def role_checker(
        current_user: User = Depends(get_current_user)
    ):
        if current_user.role != required_role:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Insufficient permissions"
            )

        return current_user

    return role_checker

Usage:

current_user: User = Depends(
    require_role("admin")
)

This means:

Only users whose role is "admin" can access this endpoint.

5. Multiple Roles

We generalized it further:

def require_roles(required_roles: list[str]):

    def role_checker(
        current_user: User = Depends(get_current_user)
    ):
        if current_user.role not in required_roles:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Insufficient permissions"
            )

        return current_user

    return role_checker

Usage:

current_user: User = Depends(
    require_roles(["admin", "teacher"])
)

This means:

admin   → ✅
teacher → ✅
student → ❌

It is OR, not AND.

6. Never Trust the Client for Roles

❌ Bad:

role = request.role

A malicious user could send:

{
    "role": "admin"
}

Instead, the role should come from the authenticated user stored in the database.

JWT
 ↓
User identity
 ↓
Database
 ↓
User.role
 ↓
Permission check
7. Important Security Rule

When creating a user, don't allow the client to decide their role:

new_user = User(
    username=user.username,
    email=user.email,
    hashed_password=hashed_password
)

The database default:

role = Column(
    String,
    default="student",
    nullable=False
)

makes new users students by default.

An administrator can later assign an appropriate role.

8. Final Day 58 Architecture
                    ┌──────────────┐
                    │   Request    │
                    └──────┬───────┘
                           ↓
                    ┌──────────────┐
                    │     JWT      │
                    └──────┬───────┘
                           ↓
                 ┌──────────────────┐
                 │ get_current_user │
                 └────────┬─────────┘
                          ↓
                    ┌────────────┐
                    │    User    │
                    └─────┬──────┘
                          ↓
                       role
                          ↓
             ┌──────────────────────┐
             │  require_role(s)     │
             └──────────┬───────────┘
                        ↓
                  Permission
                        ↓
                    Endpoint
