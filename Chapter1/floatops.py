import sys
import stdio


a, b = map(float, sys.argv[1:3])

total = a + b
diff = a - b
prod = a * b
quot = a / b
exp = a ** b

stdio.writeln(str(a) + " + " + str(b) + " = " + str(total))
stdio.writeln(str(a) + " - " + str(b) + " = " + str(diff))
stdio.writeln(str(a) + " * " + str(b) + " = " + str(prod))
stdio.writeln(str(a) + " / " + str(b) + " = " + str(quot))
stdio.writeln(str(a) + " ** " + str(b) + " = " + str(exp))
