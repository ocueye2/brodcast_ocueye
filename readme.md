# Brodcast

## what is this
Do you know the scrach brodcast block, its that but in python

## documentation
<table>
<tr>
    <th> function </th>
    <th> action </th>
    <th> example </th>
</tr>
<tr>
    <th> @brodcast.on(name) </th>
    <th> Put this above the function you want to activate with brodcast
    replace the name variable with the name you want the variable to call said function </th>
    <th>

    @brodcast.on("test") 
        def check(): 
            print("this works")

    brodcast.cont("test") 
    
</tr>
<tr>
    <th> brodcast.cont(name) </th>
    <th> This command will activate all fuctions assigned to the name variable and continue withount waiting </th>
    <th>

    import time

    @brodcast.on("test") 
        def check(): 
            time.sleep(1)
            print("This is second")

    brodcast.cont("test") 
    print("This is first")

</tr>
<tr>
    <th> brodcast.wait(name) </th>
    <th> This command is like brodcast.con but will wait for all of the functions to finish before continueing </th>
    <th>

    import time

    @brodcast.on("test") 
    def check(): 
        time.sleep(1)
        print("This is first")

    brodcast.cont("test") 
    print("This is second")

</tr>

<tr>
    <th> brodcast.debug() </th>
    <th> This command is used for </th>
    <th>


    
    @brodcast.on("a")
    def my_func():
        print("this function exists")

    if "a" in brodcast.debug():
        print("you should see this")
        # this tag is on my_func
    
    if "b" in brodcast.debug():
        print("and not this")
        # this tag is on nothing

</tr>
</table>

## brodcast also supports threding aplications

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
        

    brodcast.wait("test")  
    print()
    print("done")
    # outputs a, b, c, then done


    
