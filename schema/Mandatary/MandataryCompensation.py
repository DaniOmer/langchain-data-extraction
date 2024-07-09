from typing import List
from langchain_core.pydantic_v1 import BaseModel, Field

class MandataryCompensation(BaseModel):
    """
        Provide a detailed summary of the compensation of each named non employee director
        during the year including salary, bonus, stock awards, fees earned, all other 
        compensation and total compensation.
    """

    name: str = Field(
        ..., description="The full name of the non employee director"
    )
    year: str = Field(
        ..., description="The year the compensation is related to"
    )
    salary: str = Field(
        ..., description="The salary of the non employee director.  Returns 0 if not find"
    )
    bonus: str = Field(
        ...,
        description="The bonus of the non employee director. Returns 0 if not find",
    )
    stock_awards: str = Field(
        ..., description="The Stock Awards of the non employee director as specified in the text. Returns 0 if not find"
    )
    other_compensation: str = Field(
        ..., description= "Other Compensation earned by the non employee director. Returns 0 if not find"
    )
    total_compensation: str = Field(
        ..., description= "Total Compensation earned by the non employee director. Returns 0 if not find"
    )

class ExtractionData(BaseModel):
    """Extracted relevant information about executive officers compensation"""

    mandatary_compensations: List[MandataryCompensation]