from pydantic import BaseModel
class product(BaseModel):
    id:int
    name:str
    price:float
    in_stock:bool=True
p_1=product(id=1,name="Laptop",price=24.33,in_stock=True)
p_2=product(id=2,name="Mouse",price=23)
#p_3=product(name="keyboard")
print(p_1)
print(p_2)
#print(p_3)#