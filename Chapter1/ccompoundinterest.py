import sys
import math
import stdio


P, r, t = map(float, sys.argv[1:4])

received_sum = P * math.e ** (r*t)

stdio.writeln("Investment sum: " + str(P) + "$"+"\n" +
              "Interest rate: " + str(r * 100) + "%" + "\n" +
              "Time period: " + str(t) + "\n" +
              "-"*30 + "\n" +
              "Received sum: " + str(received_sum))
