l = []
L = []
num = int(input("input quantity number:\t"))
for i in range(num):
    n = int(input(f"input number {i + 1}:\t "))
    l.append(n)
for a in l:
    x = lambda k : k ** 2
    L.append(x(a))
print(L)
