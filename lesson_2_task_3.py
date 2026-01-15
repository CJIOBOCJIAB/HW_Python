import math
def square(a):
    return math.ceil(a*a)
side = int (input ("сторона квадрата "))
result = square(side)
print(f"площадь квадрата = {result}")
