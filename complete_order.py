class InvalidChaiError(Exception):pass
def bill(flavor,cups):
    menu={"masala":20,"ginger":40}
    try:
        if flavor not in menu:
            raise InvalidChaiError("That chai is not available")
        if not isinstance(cups,int):
            raise TypeError("NUmber of cps must be in integer")
        total=menu[flavor]*cups
        print(f"Your bill for {cups} cup of {flavor} chai: rupees {total}")
    except Exception as e:
        print("Error:",e)
    finally:
        print("Thank you for vsiting.....")   
bill("mint",2)
bill("masala","three") 
bill("ginger",4)            