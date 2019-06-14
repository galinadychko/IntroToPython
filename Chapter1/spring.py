import sys
import stdio

m, d = map(int, sys.argv[1:3])

isSpring = ((m == 3 and d >= 20 and d <= 31) or
            (m == 4 and d >= 1 and d <= 30) or
            (m == 5 and d >= 1 and d <= 31) or
            (m == 6 and d >= 1 and d <= 20))

stdio.writeln(isSpring)
