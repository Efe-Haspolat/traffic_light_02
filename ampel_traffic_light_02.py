from time import *

state3 = "ROT"
state2 = "YELLOW"
state1 = "GREEN"

mainState = state2
prevState = state3

state3_time = 10
state2_time = 2
state1_time = 15

counter_time = 0

def stateTime():
    global counter_time
    counter_time += 1
    return counter_time


while True:
    state_time = stateTime()
    if mainState == state1:
        sleep(1)
        #state_time = stateTime()
        if state_time >= state1_time and prevState == state2:
            mainState = state2
            prevState = state1
            counter_time = 0
            print(state2)


    elif mainState == state2:
        sleep(1)
        #state_time = stateTime()
        if state_time >= state2_time and prevState == state1:
            mainState = state3
            prevState = state2
            counter_time = 0
            print(state3)

        elif state_time >= state2_time and prevState == state3:
            mainState = state1
            prevState = state2
            counter_time = 0
            print(state1)


    elif mainState == state3:
        sleep(1)
        #state_time = stateTime()
        if state_time >= state3_time and prevState == state2:
            mainState = state2
            prevState = state3
            counter_time = 0
            print(state2)



