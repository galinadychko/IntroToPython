import sys
import stdio

d, m, y = map(int, sys.argv[1:4])
days_names = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

stdio.writeln("Input data:\n" + "-"*30 + "\n" +
              "day: {}, month: {}, year: {}".format(d, m, y) + "\n" +
              "-"*30)

y_0 = y - (14 - m) // 12
x = y_0 + y_0 // 4 - y_0 // 100 + y_0 // 400
m_0 = m + 12 * ((14 - m) // 12) - 2
d_0 = (d + x + (31*m_0) // 12) % 7

stdio.writeln("Day of week: " + days_names[d_0])
