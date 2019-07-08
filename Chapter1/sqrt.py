import sys
import stdio

c, epsilon = float(sys.argv[1]), float(sys.argv[2])

x0 = c

# By Newton definition
# ---------------------
# f_x0 = x0**2 - c
# df_dx = 2 * x0
#
# while abs(f_x0) > epsilon:
#     x0 = x0 - f_x0 / df_dx
#     f_x0 = x0 ** 2 - c
#     df_dx = 2 * x0
#
# stdio.writeln("sqrt(" + str(c) + ") = " + str(x0))


# After substitution f_x0  and derivative values
while abs(x0 ** 2 - c) > epsilon:
    x0 = x0 - (x0 - c / x0) / 2

stdio.writeln("sqrt(" + str(c) + ") = " + str(x0))