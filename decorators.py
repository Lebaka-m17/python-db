from functools import wraps
def my_decorator(func):
    @wraps(func)
    def wrapper():
        print("Before function runs")
        func()
        print("After function runs")
    return wrapper



@my_decorator 
def greet():
    print("Hello from decorators") 


greet()
print(greet.__name__)
#build a logger with decorator
from functools import wraps
def log_activity(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f" Calling: {func.__name__}")
        result=func(*args, **kwargs)
        print(f"✅ Finished:{func.__name__}")
        return result
    return wrapper

@log_activity
def brew_chai(type,milk="no"):
    print(f"Brewing {type} chai and milk status {milk}")
brew_chai("Masala")  

#
from functools import wraps
def require_admin(func):
    @wraps(func)
    def wrapper(user_role):
        if user_role!="admin":
            print("Access denied: Admins only")
            return None
        else:
            return func(user_role)
    return wrapper
@require_admin
def access_tea_inventory(role):
    print("Access granted to tea inventory") 
access_tea_inventory("user")          
access_tea_inventory("admin")