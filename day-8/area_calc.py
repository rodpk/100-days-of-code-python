import math
# number of cans = (h x w) / coverage per can (5)
# should round up.


def calc(height, width, coverage):
    answr =  ((height * width) / coverage)
    return math.ceil(answr)







height = int(input('Height of the wall: '))
width = int(input('Width of the wall: '))
coverage = 5

print(calc(height, width, coverage))
