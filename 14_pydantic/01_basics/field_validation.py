from pydantic import BaseModel, field_validator
class User(BaseModel):
    username:str
    @field_validator('username')
    def username_length(cla,v):
        if(len(v)<4):
            raise ValueError("Username must be at least 4 characters")
        return v