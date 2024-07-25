from typing import List
from langchain_core.pydantic_v1 import BaseModel, Field

class Person(BaseModel):
    "Provide a relevant informations about the person including name, age, resume."

    name: str = Field(
        ..., description=f"The full name of the person"
    )
    gender: str = Field(
        ..., description=f"The gender of the person. Is the person a male (M) or female (F)?"
    )
    date_birth: str = Field(
        ...,
        description=f"The year of birth of the person.",
    )
    resume: str = Field(
        ...,
        description=f"The resume telling who is the person in 200 words.",
    )

class ExtractionData(BaseModel):
    f"Extracted relevant information about the person."

    person: List[Person]