from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Welcome to my first FastAPI server!"}


@app.get("/about")
def about():
    return {
        "name": "Surya Rathore",
        "college": "IIITDM Jabalpur",
        "branch": "Smart Manufacturing"
    }


@app.get("/skills")
def skills():
    return {
        "skills": [
            "Python",
            "C++",
            "DSA",
            "Machine Learning",
            "FastAPI"
        ]
    }