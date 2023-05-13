import math
l = []
num = int(input("input quantity number:\t"))
for i in range(num):
    n = int(input(f"input number {i + 1}:\t "))
    l.append(n)
L = [math.sqrt(n) for n in l]
print(L)