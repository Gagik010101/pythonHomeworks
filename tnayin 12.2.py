def Sum(L, S):
    try:
        for h in L:
            S += h
        return S
    except(TypeError):
        return None



L = [5, 8, "hello", 257, 777]
S = 0
print(Sum(L, S))