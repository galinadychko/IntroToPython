import sys
import math
import stdio


a, b, c = map(int, sys.argv[1:4])

stdio.writeln(not (math.fabs(a - b) < c < a + b))
