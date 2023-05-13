def separation(num1, num2):
    try:
        S = num1 / num2
        return S
    except(ZeroDivisionError):
        return None







num1 = int(input("input first number:\t"))
num2 = int(input("input second number:\t"))
print(separation(num1, num2))