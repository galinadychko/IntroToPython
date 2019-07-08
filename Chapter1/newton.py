import sys
import stdio


x_0, epsilon = int(sys.argv[1]), float(sys.argv[2])

f_x_0 = x_0 ** 2 - 4
df_dx_x0 = 2 * x_0
i = 1

stdio.writeln("-" * 25 + "\n" +
              "Function: f(x) = x^2" + "\n"
              "Initial start: x_0 = " + str(x_0) + "\n" +
              "-" * 25 + "\n")

while abs(f_x_0) > epsilon:
    stdio.writeln("Step: " + str(i) + ":" + "\n" +
                  "x_" + str(i) + "=" + str(x_0) + "\n" +
                  "f(x_" + str(i) + ")=" + str(f_x_0) + "\n" +
                  "df/dx (x_" + str(i) + ")=" + str(df_dx_x0) + "\n" +
                  "-" * 40)
    # y = k * x + b
    b = f_x_0 - df_dx_x0 * x_0
    x_0 = - b / df_dx_x0
    f_x_0 = x_0 ** 2 - 4
    df_dx_x0 = 2 * x_0
    i += 1


