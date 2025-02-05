import time

change = False

@brodcast.on("test")
def my_func():
    global change
    print("a")
    change = True
    while change:
        time.sleep(.1)
    print("c")

@brodcast.on("test")
def my_func2():
    global change
    while not change:
        time.sleep(.1)
    print("b")
    change = False
    

brodcast.debug()  # Check registered functions
brodcast.wait("test")  # Execute functions
print()
print("done")
print()
brodcast.cont("test") 
brodcast.cont("test") 

