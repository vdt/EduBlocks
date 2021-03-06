import random
import subprocess
import time
from threading import Condition, Event, Thread

from psonic import *

from mcpi import block as block

BlocksList = [1,2,3,4,5,7,12,13,14,15,16,17,18,20,21,22,24,41,42,45,46,47,49]
WoolList = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]


def PixelArt(N1,N2,N3,N4,N5,N6,N7,N8,
             N9,N10,N11,N12,N13,N14,N15,N16,
             N17,N18,N19,N20,N21,N22,N23,N24,
             N25,N26,N27,N28,N29,N30,N31,N32,
             N33,N34,N35,N36,N37,N38,N39,N40,
             N41,N42,N43,N44,N45,N46,N47,N48,
             N49,N50,N51,N52,N53,N54,N55,N56,
             N57,N58,N59,N60,N61,N62,N63,N64):
    
    row0 = [N1,N2,N3,N4,N5,N6,N7,N8]#1-8
    row1 = [N9,N10,N11,N12,N13,N14,N15,N16]
    row2 = [N17,N18,N19,N20,N21,N22,N23,N24]
    row3 = [N25,N26,N27,N28,N29,N30,N31,N32]
    row4 = [N33,N34,N35,N36,N37,N38,N39,N40]
    row5 = [N41,N42,N43,N44,N45,N46,N47,N48]
    row6 = [N49,N50,N51,N52,N53,N54,N55,N56]
    row7 = [N57,N58,N59,N60,N61,N62,N63,N64]
    
    List = [row7,row6,row5,row4,row3,row2,row1,row0]
    return List

def PrintWall(ImportedList):

    pos = mc.player.getTilePos()
    mc.player.setPos(pos.x,pos.y,pos.z)

    myList = ImportedList
    

    for row in range (0,8):
        for column in range (0,8):
            
            mc.setBlock(pos.x+column,pos.y+row,pos.z-20,myList[row][column]) 

def distance_to_player(x, y, z):
  global mc, math
  pp = mc.player.getPos()
  xd = x - pp.x
  yd = y - pp.y
  zd = z - pp.z
  return math.sqrt((xd * xd) + (yd * yd) + (zd * zd))


def live_loop_1():
    pass

def live_loop_2():
    pass

def live_loop_3():
    pass

def live_loop_4():
    pass

def live_loop_1a(condition,stop_event):
    while not stop_event.is_set():
        with condition:
            condition.notifyAll() #Message to threads
        live_loop_1()

def live_loop_2a(condition,stop_event):
    while not stop_event.is_set():
        with condition:
            condition.wait() #Wait for message
        live_loop_2()

def live_loop_3a(condition,stop_event):
    while not stop_event.is_set():
        with condition:
            condition.wait() #Wait for message
        live_loop_3()

def live_loop_4a(condition,stop_event):
    while not stop_event.is_set():
        with condition:
            condition.wait() #Wait for message
        live_loop_4()

condition = Condition()
stop_event = Event()
live_thread_1 = Thread(name='producer', target=live_loop_1a, args=(condition,stop_event))
live_thread_2 = Thread(name='consumer1', target=live_loop_2a, args=(condition,stop_event))
live_thread_3 = Thread(name='consumer2', target=live_loop_3a, args=(condition,stop_event))
live_thread_4 = Thread(name='consumer3', target=live_loop_4a, args=(condition,stop_event))

# live_thread_1.start()
# live_thread_2.start()
# live_thread_3.start()
# live_thread_4.start()


def buildPumpkin(x, y, z):
  mc.setBlocks(x-2, y-2, z-2, x+2, y+2, z+2, 35, 1)
  mc.setBlocks(x-1, y-1, z-1, x+1, y+1, z+1, 0, 1)
  mc.setBlock(x-1, y+1, z-2, 0)
  mc.setBlock(x+1, y+1, z-2, 0)

  mc.setBlocks(x+1, y-1, z-2, x-1, y-1, z-2, 0, 0)
  mc.setBlock(x-1, y+1, z+2, 0)
  mc.setBlock(x+1, y+1, z+2, 0)

  mc.setBlocks(x+1, y-1, z+2, x-1, y-1, z+2, 0, 0)
  mc.setBlock(x-2, y+1, z-1, 0)
  mc.setBlock(x-2, y+1, z+1, 0)

  mc.setBlocks(x-2, y-1, z+1, x-2, y-1, z-1, 0, 0)
  mc.setBlock(x+2, y+1, z-1, 0)
  mc.setBlock(x+2, y+1, z+1, 0)

  mc.setBlocks(x+2, y-1, z+1, x+2, y-1, z-1, 0, 0)
  mc.setBlock(x, y+3, z, 35, 5)

old_print = print

# Overload print so that we can't hammer the standard output.
# Print is limited to 1 line every 1/10 seconds.
def print(*args):
  old_print(*args)
  time.sleep(0.10)

print('[Starting]')
print()
