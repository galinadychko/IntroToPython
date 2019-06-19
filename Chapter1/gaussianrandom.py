import random
import math
import stdio


u, v = random.random(), random.random()
w = math.sin(2*math.pi*v) * (-2*math.log(u)) ** (1/2)

stdio.writeln("Random values is " + str(w))
