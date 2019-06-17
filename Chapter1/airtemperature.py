import sys
import stdio

stdio.writeln("-"*45)
stdio.writeln("!!!Remarks!!!\nInput parameters should satisfy:\n1) |t| < 50\n2) 3 < v < 120")
stdio.writeln("-"*45)

T, v = map(float, sys.argv[1:3])
w = 35.74 + .6215 * T + (.4275 * T - 35.75) * v ** .16

stdio.writeln("Input:\n" +
              "Temperature: {}F\n".format(T) +
              "Wind velocity: {}m/h\n".format(v))
stdio.writeln("-"*45)
stdio.writeln("Air temperature: {}F".format(w))
