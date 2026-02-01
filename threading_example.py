import threading
import time
def order_chai():
    for i in range(1,4):
        print(f"Taking order for:{i}")
        time.sleep(2)
def brew_chai():
    for i in range(1,4):
        print(f"Brewing chai for : {i}")  
        time.sleep(3)
#creating threads and giving the targets        
order_thread=threading.Thread(target=order_chai)  
brew_thread=threading.Thread(target=brew_chai)
#start
order_thread.start()
brew_thread.start()
# joining  them together until thier processing
order_thread.join()
brew_thread.join()
print(f"All orders are taken and brewed")
