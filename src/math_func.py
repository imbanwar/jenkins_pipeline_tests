import os
def add(x, y=2):
    print(x + y)
    print("addition completed")
    return x + y
def product(x, y=2):
    print(x * y)
    print("multiplication completed")
    return x * y
input1 = int(os.getenv("value1"))
input2 = int(os.getenv("value2"))
add(input1, input2)
product(input1, input2)
