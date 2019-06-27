import sys
import math
import stdio

x1, y1, x2, y2 = map(lambda x: math.radians(float(x)), sys.argv[1:5])

angle = math.acos(math.sin(x1) * math.sin(x2) +
                   math.cos(x1) * math.cos(x2) * math.cos(y1 - y2))
d = 60 * math.degrees(angle)

stdio.writeln("The input data:" + "\n" +
              "-" * 40 + "\n" +
              "(x1, y1) = ({}, {})".format(sys.argv[1], sys.argv[2]) + "\n" +
              "(x2, y2) = ({}, {})".format(sys.argv[3], sys.argv[4]) + "\n" +
              "-" * 40 + "\n" +
              "Great-circle distance is {}".format(d))
