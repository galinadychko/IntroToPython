import stdio
import random

random_values = tuple(map(lambda x: random.random(), range(5)))

stdio.writeln("Random values: " + "\n" +
              "-" * 30 + "\n"
              "{}".format(random_values) + "\n" +
              "-" * 100 + "\n" +
              "mean: {}".format(sum(random_values) / 5) + "\n"
              "min: {}".format(min(random_values)) + "\n" +
              "max: {}".format(max(random_values)) + "\n")
