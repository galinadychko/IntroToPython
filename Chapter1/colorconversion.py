import sys
import stdio


r, g, b = map(int, sys.argv[1:4])

is_zero = (r == 0) | (g == 0) | (b == 0)

w = max((r / 255, g/255, b/255))
c = (w - (r/255)) / (w or is_zero)
m = (w - (g/255)) / (w or is_zero)
y = (w - (b/255)) / (w or is_zero)

k = 1 - w

stdio.writeln("Input data:" + "\n" +
              "-" * 30 + "\n" +
              "Red: {}, Green: {}, Blue: {}".format(r, g, b) + "\n" +
              "-" * 30 + "\n" +
              "CMYK" + "\n" +
              "c: " + str(c) + "\n" +
              "m: " + str(m) + "\n" +
              "y: " + str(y) + "\n" +
              "k: " + str(k) + "\n")
