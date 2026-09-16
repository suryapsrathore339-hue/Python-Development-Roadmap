from sqlalchemy import Column, Integer, String

from database import Base


class Student(Base):
    __tablename__ = "students"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    name = Column(
        String,
        nullable=False
    )

    age = Column(
        Integer,
        nullable=False
    )

    branch = Column(
        String,
        nullable=False
    )

# Student
created_by = Column(
    Integer,
    ForeignKey("users.id"),
    nullable=True
)

creator = relationship(
    "User",
    back_populates="students"
)