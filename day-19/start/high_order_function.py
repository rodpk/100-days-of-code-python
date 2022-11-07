def add(n1, n2):
    return n1+n2
def subtract(n1, n2):
    return n1-n2


def calculator(n1, n2, function):
    return function(n1, n2)



result = calculator(10, 20, add)


print(f"Result is {result}")