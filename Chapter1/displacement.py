import sys
import stdio

G = 9.80665
x_0, v_0, t = map(float, sys.argv[1:4])
displacement = x_0 + v_0 * t - G * t ** 2 / 2

stdio.writeln("|" + "-"*35 + "|" + "\n" +
              "| Object was thrown straight up     |\n" +
              "|" + "-"*35 + "|" + "\n" +
              "| from position: {}\n| with velocity:   {} m/s\n".format(x_0, v_0) +
              "|" + "-"*35 + "|" + "\n" +
              "| After {}s \n| displaces at {}m".format(t, displacement) +
              " "*11 + "|\n" +
              "|" + "-"*35 + "|")
