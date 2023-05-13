def IError(L):
    try:
        x1 = L[0]
        x2 = L[-1]
        H = x1 * x2
        return H
    except(IndexError,TypeError):
        return None




L = []
num = input("input quantity number")
L.append(num)
print(IError(L))