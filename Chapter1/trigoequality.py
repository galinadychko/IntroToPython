import sys
import math
import stdio

theta = float(sys.argv[1])

value = (math.sin(theta)) ** 2 + (math.cos(theta)) ** 2

stdio.writeln(str(value))
