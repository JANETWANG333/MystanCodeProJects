"""
File: DoubleBeepers.py
Name:
-------------------------------
"""

from karel.stanfordkarel import *


def main():
    """
    Karel will double the beepers
    """
    if front_is_clear():
        move()
    if on_beeper():
        pick_beeper()
        Doublebeepers()
        MoveToTheEnd()


def Doublebeeper():
    count = 1
    while on_beeper():
        pick_beeper()
        count += 1 #count = count + 1
    count *= 2 #count = count *2
    #for int i =0; i < count; i += 1
    for i in range(count):
        put_beeper()


def MoveToTheEnd():
    while front_is_clear():
        move()
        
    
        
        


# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
