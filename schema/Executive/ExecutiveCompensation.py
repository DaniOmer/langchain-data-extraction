from typing import List
from langchain_core.pydantic_v1 import BaseModel, Field

class ExecutiveCompensation(BaseModel):
    """
        Provide a complete list of executive officers according to the executive compensation table.
        I want you to retrieve only executive officers present in the text for the most recent year.
    """
    # """
    #     Provide a detailed summary of the compensation of each named executive officer
    #     during the year including salary, bonus, stock awards, fees earned, all other 
    #     compensation and total compensation.
    # """

    name: str = Field(
        ...,
        description="The full name of the executive officer"
    )
    position: str = Field(
        ..., description="The job title or position of the executive officer"
    )
    gender: str = Field(
        ..., description="The gender of the executive officer. Is the executive officer a male (M) or female (F)?"
    )
    salary: str = Field(
        default="0",
        description="The salary of the executive officer.  Returns 0 if not find"
    )
    bonus: str = Field(
        default="0",
        description="The bonus of the executive officer. Returns 0 if not find",
    )
    stock_awards: str = Field(
        default="0",
        description="The Stock Awards of the executive officer as specified in the text. Returns 0 if not find"
    )
    other_compensation: str = Field(
        default="0",
        description= "Other Compensation earned by the executive officer. Returns 0 if not find"
    )
    total_compensation: str = Field(
        default="0",
        description= "Total Compensation earned by the executive officer. Returns 0 if not find"
    )


class ExtractionData(BaseModel):
    """Extracted relevant informations about executive officers and their compensation."""

    executive_compensations: List[ExecutiveCompensation]