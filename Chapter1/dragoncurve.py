import stdio


order0 = "F"
noorder0 = "F"

order1 = order0 + "L" + noorder0
noorder1 = order0 + "R" + noorder0

order2 = order1 + "L" + noorder1
noorder2 = order1 + "R" + noorder1

order3 = order2 + "L" + noorder2
noorder3 = order2 + "R" + noorder2

order4 = order3 + "L" + noorder3
noorder4 = order3 + "R" + noorder3

order5 = order4 + "L" + noorder4

name = "dragon curve"

stdio.writeln("0-" + name + ": " + order0 + "\n" +
              "1-" + name + ": " + order1 + "\n" +
              "2-" + name + ": " + order2 + "\n" +
              "3-" + name + ": " + order3 + "\n" +
              "4-" + name + ": " + order4 + "\n" +
              "5-" + name + ": " + order5 + "\n")
