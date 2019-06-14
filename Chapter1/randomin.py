import sys
import random
import stdio

a, b = map(int, sys.argv[1:3])

stdio.writeln(random.randrange(a, b))
