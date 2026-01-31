#try except
chai_menu={"masala":30,"ginger":40}
try:
    chai_menu["elaichi"]
except KeyError:
    print("The key that you are trying not exists")    
print("hello chai code")
#complex_try
def serve_chai(flavor):
    try:
        print(f"Preparing {flavor} chai...")
        if flavor=="unknown":
            raise ValueError("We don't know that flavor")
    except ValueError as e:
        print("Error:",e)
    else:
        print(f"{flavor} chai is served")
    finally:
        print("Next customer please!!")
serve_chai("MAsala")
serve_chai("Lemon")            
serve_chai("unknown")
#multiple execptions
def process_order(item,quantity):
    try:
        price={"masala":20}[item]
        cost=price*quantity
        print(f"total cost is {cost}")
    except KeyError:
        print("Sorry that chai is not in the menu")
    except TypeError:
        print("Qunatity must be in number")
process_order("ginger",2)
process_order("masala","two")   
#custom errors
def brew_chai(flavor):
    if flavor not in ["masala", "ginger", "elaichai"]:
        raise ValueError("Unsupported chai flavor...")
    print(f"brewing {flavor} chai...")


brew_chai("mint")
# custom Exceptionss
class OutOfIngredientsError(Exception):
    pass
def make_chai(milk,sugar):
    if milk==0 or sugar==0:
        raise OutOfIngredientsError("Missing")
    print("chai is ready!!!")
make_chai(0,0)    
           



