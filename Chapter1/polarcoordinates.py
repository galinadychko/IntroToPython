import sys
import math
import stdio

x, y = map(float, sys.argv[1:3])

r = math.sqrt(x ** 2 + y ** 2)
theta = math.atan2(y, x)

stdio.writeln("Input:\n" +
              "-"*6 + "\n" +
              "x:{}\n".format(x) +
              "y:{}\n".format(y) +
              "-"*15)
stdio.writeln("In polar system:\n" +
              "-"*15 + "\n" +
              "r:" + str(r) + " theta:" + str(theta))
