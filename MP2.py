from turtle import *

try :
     reset()
except Terminator:
    pass
setup (600 ,400)

def triangle():
    left(60)
    forward(20)
    right(120)
    forward(20)
    
for i in range(15):
    
    forward(20)
    for i in range(3):
        triangle()
    left(60)
    forward(20)
    left(60)
