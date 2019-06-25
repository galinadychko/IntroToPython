import sys
import math
import stdio


_lambda0, _phi, _lambda = map(float, sys.argv[1:4])
x = math.log((1 + math.sin(_phi))/(1 - math.sin(_phi))) / 2
y = (_lambda - x) / _lambda0

stdio.writeln("Input data:" + "\n" +
              "-" * 40 + "\n" +
              "longitude of the map center point: {}".format(_lambda0) + "\n" +
              "latitude: {}".format(_phi) + "\n" +
              "longitude: {}".format(_lambda) + "\n" +
              "-" * 40 + "\n" +
              "Rectangular coordinates:" + "\n" +
              "-" * 40 + "\n" +
              "x: {}, y: {}".format(x, y))

