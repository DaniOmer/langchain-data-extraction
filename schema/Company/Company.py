from typing import List
from langchain_core.pydantic_v1 import BaseModel, Field

class Company(BaseModel):
    """
        Provide a detailed summary of the company's key information according to the text.
        I want you to include the following details:
        - Company name
        - Industry/sector
        - Headquarters location
        - Year of establishment
        - Number of employees
        - Annual revenue
        - Stock ticker symbol (if publicly traded)
        - company auditor
    """


    denomination: str = Field(
        ...,
        description="The full name of the company."
    )
    since: str = Field(
        ..., description="Year of establishment, the year the company was founded."
    )
    site: str = Field(
        ..., description="The company website."
    )
    address: str = Field(
        ..., description="The company full address."
    )
    effective: str = Field(
        default="N/A",
        description="The number of employees or workforce of the company."
    )
    auditors: str = Field(
        default="N/A",
        description="The name of the company appointed as auditors for the company. Here are some examples : 'KPMG, Ernst & Young LLP, PricewaterhouseCoopers LLP, Deloitte & Touche LLP,...'."
    )
    resume: str = Field(
        ...,
        description="The resume telling what is the company about in 300 words."
    )
    capitalisation: str = Field(
        default="N/A",
        description= "The company capitalisation."
    )
    market: str = Field(
        default="N/A",
        description= "The stock market that the company is associated with."
    )


class ExtractionData(BaseModel):
    """Extracted relevant informations about executive officers and their compensation."""

    company: List[Company]