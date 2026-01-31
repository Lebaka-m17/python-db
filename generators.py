#genarators
def serve_chai():
    yield "Cup1:Masala Chai"
    yield "Cup2:Ginger chai"
stall=serve_chai()
for cup in stall:
    print(cup)    

#using next to get value

def get_chai_gen():
    yield "Cup1"
    yield "Cup2"
    yield "cup3"
chai=get_chai_gen()
print(next(chai))  
#infinite 
def infinite_cake():
    count=1
    while True:
        yield f"Make :{count}" 
        count+=1
Make=infinite_cake()
for _ in range(5):
    print(next(Make)) 
#send values
def Cake_customer():
    print("Welcome ! what cake would you like?")
    order=yield
    while True:
        print("Preparing:", (order))
        order=yield
Bakery=Cake_customer()
next(Bakery)
Bakery.send("Chaco cake")
Bakery.send("Honey  cake") 
#yield close and from
def local_cake():
    yield "Honey cake"
    yield "Cahacolate cake"
def imported_cake():
    yield "Oreo cake"
    yield "Brownie" 

def full_menu():
    yield from local_cake()
    yield from imported_cake()
for cake in full_menu():
    print(cake)

#close
def chai_stall():
    try:
        while True:
            order=yield "Waiting for chai order"
    except:
        print("Stall closed ,No more chai")
stall=chai_stall()
print(next(stall))
stall.close()                

       
