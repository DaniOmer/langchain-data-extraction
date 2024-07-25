from typing import List
from langchain_core.pydantic_v1 import BaseModel, Field

class MandataryCompensation(BaseModel):
    """
        Provide a complete list of each Non-Employee Director (also known as a board director or director nominee) 
        who served on the Board during the year. I want you to retrieve each person mention as board director in the 
        text.
    """

    name: str = Field(
        ..., description="The full name of the non employee director"
    )
    gender: str = Field(
        ..., description="The gender of the non employee director. Is the non employee director a male (M) or female (F)?"
    )
    salary: str = Field(
        default="0",
        description="The salary or fees earned or paid in cash of the non employee director.",
    )
    bonus: str = Field(
        default="0",
        description="The bonus of the non employee director.",
    )
    stock_awards: str = Field(
        default="0",
        description="The Stock Awards, also known as option awards, of the non employee director as specified in the text."
    )
    other_compensation: str = Field(
        default="0",
        description= "Other Compensation earned by the non employee director."
    )
    total_compensation: str = Field(
        default="0",
        description= "Total Compensation earned by the non employee director."
    )

class ExtractionData(BaseModel):
    """Extracted relevant information about non employee director compensation."""

    mandatary_compensations: List[MandataryCompensation]