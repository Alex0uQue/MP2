from turtle import *

try :
     reset()
except Terminator:
    pass
setup (1380 ,180)

def triangle():
    left(60)
    forward(10)
    right(120)
    forward(10)
for i in range(10):   
    for i in range(3):
    
        forward(10)
        for i in range(3):
            triangle()
        left(60)
        forward(10)
        left(60)


    forward(10)
    triangle()
    left(60)
    forward(10)
    left(60)
    forward(10)
    triangle()
    left(60)
    forward(10)
    left(60)