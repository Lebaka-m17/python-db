#nonlocal
def update_order():
    cake_type="Chaco"
    def kitchen():
        nonlocal cake_type
        cake_type="Oreo"
    kitchen()
    print("After Update:",cake_type)
update_order() 
#global
coffee_typr="Plain"
def front_desk():
    def kitchen():
        global coffee_type
        coffee_type="Strong"
    kitchen()
    print("After kitchen update",coffee_type)
front_desk()               
