from typing import Optional
from pydantic import BaseModel,Field
import re
class Employee(BaseModel):
    id:int
    name:str=Field(
        ...,
        min_length=3,
        max_length=59,
        description="Employee Name",
        json_schema_extra={"example":"Mahija"}

    )
    department:Optional[str]='General'
    salary:float=Field(
        ...,
        ge=10000,
        lt=1000000,
        description="Annaual salary",
        json_schema_extra={"example":"salary"}

    ) 

