import sys
import math
import stdio

t = float(sys.argv[1])

stdio.writeln("sin(2*{}) + sin(3*{}) = {}".format(t, t, math.sin(2*t) + math.sin(3*t)))
