class Cake:
    pass
class CakeTime:
    pass


print(type(Cake))
Chaco_cake=Cake()
print(type(Chaco_cake))
print(type(Chaco_cake) is Cake)
print(type(Chaco_cake) is CakeTime)
#class and object namespace
class Cake:
    origin="India"
print(Cake.origin)
Cake.is_cool=False
print(Cake.is_cool)
#
chaco=Cake()
print(chaco.origin)
print(chaco.is_cool)
Cake.is_cool=True
print("Class:",Cake.is_cool)
#attribute shadowing
class Chai:
    temp="Hot"
    strngth="strong"

cutting=Chai()
print(cutting.temp)
cutting.temp="Mild"
print(f"after change:",cutting.temp)
print(f"Before :",Chai.temp)
del cutting.temp
print(cutting.temp)
#self args
class Chaicup:
    size=150
    def describe(self):
        return f"A {self.size} ml of cup"
    
cup=Chaicup()
print(cup.describe())
print(Chaicup.describe(cup))
#init
class ChaiOrder:
    type=None
    def __init__(self,type_,size):
        self.type=type_
        pass
