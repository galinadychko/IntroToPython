import math
import sys
import stdio


b, c = map(float, sys.argv[1:3])

discriminant = b ** 2 - 4 * c
d = math.sqrt(discriminant)

stdio.writeln(str((-b + d) / 2))
stdio.writeln(str((-b - d) / 2))
