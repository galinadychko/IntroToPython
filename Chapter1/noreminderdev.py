import sys
import stdio

a, b = map(int, sys.argv[1:3])

stdio.writeln(a % b == 0)