import os
def add(a, b):
	print("Gong to add two number")
	print("Addition", int(a) + int(b))
input1 = os.getenv("value1")
input2 = os.getenv("value2")
add(input1, input2)