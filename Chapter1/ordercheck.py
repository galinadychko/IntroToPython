import sys
import stdio

x, y, z = map(float, sys.argv[1:4])

stdio.writeln("Input values:\n" +
              "-"*15 + "\n" +
              "x = " + str(x) + "\n" +
              "y = " + str(y) + "\n" +
              "z = " + str(z) + "\n" +
              "-"*15 + "\n" +
              "Inequalities:\n (x < y < z) or (x > y > z) are " +
              str((x < y < z) or (x > y > z)))
