from math import factorial
def Bubble_sort_list(l, L):
    for i in range(num):
        n = int(input(f"input number {i + 1}:\t "))
        l.append(n)
    Bubble_sort_filter(L, l)
def Bubble_sort_filter(L, l):
    for s in l:
        L.add(s)
    l = []
    for s in L:
        l.append(s)
    print(Bubble_sort_operation(l))
def Bubble_sort_operation(l):
    for j in range(factorial(len(l))):
        for i in l:
            n = l.index(i)
            if n == len(l)-1:
                break
            Index = n + 1
            m = l[Index]
            if i <= m:
                continue
            else:
                l[n], l[m] = l[m], l[n]
    return l
l = []
num = int(input("input quantity number:\t"))
L = set()

Bubble_sort_list(l, L)

