import datetime
from typing import List
from langchain_core.pydantic_v1 import BaseModel, Field

class MandataryCompensation(BaseModel):
    """
    Provide a complete list of each Non-Employee Director (also known as a board director or director nominee) 
    who served on the Board during the year. I want you to retrieve all the board director present in the text.
    """

    name: str = Field(
        ..., description="The full name of the non employee director"
    )
    salary: str = Field(
        default="0",
        description="The salary of the non employee director. Returns 0 if not find",
    )
    bonus: str = Field(
        default="0",
        description="The bonus of the non employee director. Returns 0 if not find",
    )
    stock_awards: str = Field(
        default="0",
        description="The Stock Awards of the non employee director as specified in the text. Returns 0 if not find"
    )
    other_compensation: str = Field(
        default="0",
        description= "Other Compensation earned by the non employee director. Returns 0 if not find"
    )
    total_compensation: str = Field(
        default="0",
        description= "Total Compensation earned by the non employee director. Returns 0 if not find"
    )

class ExtractionData(BaseModel):
    """Extracted relevant information about non employee director compensation."""

    mandatary_compensations: List[MandataryCompensation]