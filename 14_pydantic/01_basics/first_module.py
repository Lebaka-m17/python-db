from pydantic import BaseModel
class User(BaseModel):
    id: int
    name: str
    is_instance: bool
input_data={"id":12,"name":"Mahija","is_instance":True}
user=User(**input_data)
print(user)    

