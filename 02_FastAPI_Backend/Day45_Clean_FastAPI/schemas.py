from pydantic import BaseModel


class StudentRequest(BaseModel):
    name: str
    age: int
    branch: str