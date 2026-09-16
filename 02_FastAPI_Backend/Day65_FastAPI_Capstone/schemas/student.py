from pydantic import BaseModel, Field, field_validator,EmailStr

class UserInfo(BaseModel):
    username: str
    email: EmailStr

class StudentCreate(BaseModel):
    name: str = Field(min_length=2, max_length=50)
    age: int = Field(ge=16, le=100)
    branch: str = Field(min_length=2, max_length=20)

    @field_validator("name")
    @classmethod
    def validate_name(cls, value):
        value = value.strip()

        if not value:
            raise ValueError("Name cannot be empty")

        return value

    @field_validator("branch")
    @classmethod
    def normalize_branch(cls, value):
        return value.strip().upper()


class StudentResponse(BaseModel):
    id: int
    name: str
    age: int
    branch: str
    creator: UserInfo

    class Config:
        from_attributes = True