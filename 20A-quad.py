import math
import sys

print("ax2 + bx + c = 0")

a = float(input("a? "))
b = float(input("b? "))
c = float(input("c> "))

if a == 0:
    print("a = 0 : This is not 2nd equation")
    sys.exit()

D = b*b - 4*a*c

if D > 0:
    x1 = (-b+math.sqrt(D)) / (2*a)
    x2 = (-b+math.sqrt(D)) / (2*a)
    print("Two solution: ", x1, x2)

if D == 0:
    x = b / (2*a)
    print("1 solution: ", x)

if D < 0:
    print("No solution.")
