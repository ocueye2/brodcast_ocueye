import pytest
import time
from src.Brodcast_ocueye import brodcast

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

def test_brodcast_flow(capfd):
    brodcast.wait("test")  # Trigger the event
    time.sleep(0.5)  # Allow some time for execution
    assert 1 == 2

    print("done")
