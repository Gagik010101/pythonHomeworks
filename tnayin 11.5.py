H = open("b.txt", "w")
with open("poem.txt", "r") as F:
    for i in F:
        H.write(i)

