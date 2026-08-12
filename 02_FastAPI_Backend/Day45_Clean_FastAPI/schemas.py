from pydantic import BaseModel


class StudentRequest(BaseModel):
    name: str
    age: int
    branch: str

class StudentResponse(BaseModel):
    id: int
    name: str
    age: int
    branch: str

    model_config = {
        "from_attributes": True
    }

    