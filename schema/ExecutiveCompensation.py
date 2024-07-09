from langchain_core.pydantic_v1 import BaseModel, Field

class ExecutiveCompensation(BaseModel):
    """
        Provide a detailed summary of the compensation of each named executive officer
        during the year including salary, bonus, stock awards, fees earned, all other 
        compensation and total compensation.
    """

    name: str = Field(
        ..., description="The full name of the executive officer"
    )
    year: str = Field(
        ..., description="The year the compensation is related to"
    )
    salary: str = Field(
        ..., description="The salary of the executive officer.  Returns 0 if not find"
    )
    bonus: str = Field(
        ...,
        description="The bonus of the executive officer. Returns 0 if not find",
    )
    stock_awards: str = Field(
        ..., description="The Stock Awards of the executive officer as specified in the text. Returns 0 if not find"
    )
    other_compensation: str = Field(
        ..., description= "Other Compensation earned by the executive officer. Returns 0 if not find"
    )
    total_compensation: str = Field(
        ..., description= "Total Compensation earned by the executive officer. Returns 0 if not find"
    )