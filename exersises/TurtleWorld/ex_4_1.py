from swampy.TurtleWorld import *

def square(t):
    for i in range(4):
        fd(t, 100)
        lt(t)

bob = Turtle()

square(bob)
