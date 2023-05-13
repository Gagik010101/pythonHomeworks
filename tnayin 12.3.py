def Error(h):
    try:
        with open("text.txt", "r") as h:
            for i in h:
                print(i)
    except(FileNotFoundError):
        return None
h = open("text.txt", "a")
print(Error(h))