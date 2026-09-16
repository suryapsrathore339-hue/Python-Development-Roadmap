from pydantic import BaseModel, EmailStr, Field, field_validator


class UserCreate(BaseModel):
    username: str = Field(min_length=3, max_length=30)
    email: EmailStr
    password: str = Field(min_length=8, max_length=100)

    @field_validator("username")
    @classmethod
    def validate_username(cls, value):
        return value.strip()


class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr

    class Config:
        from_attributes = True