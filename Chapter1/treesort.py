import sys
import stdio

x, y, z = map(float, sys.argv[1:4])

max_value = max(x, y, z)
min_value = min(x, y, z)
median = x + y + z - max_value - min_value

stdio.writeln("Input data:" + "\n" +
              "-" * 30 + "\n" +
              "{}, {}, {}".format(x, y, z) + "\n" +
              "-" * 30 + "\n" +
              "Ascending order: {}, {}, {}".format(min_value, median, max_value))
