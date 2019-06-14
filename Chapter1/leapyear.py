import sys
import stdio

year = int(sys.argv[1])

isDivided4 = (year % 4 == 0)
isDivided100 = (year % 100 == 0)
isDivided400 = (year % 400 == 0)

isLeapYear = ((isDivided4 and not isDivided100) or (isDivided4 and isDivided100 and isDivided400))
stdio.writeln(isLeapYear)
