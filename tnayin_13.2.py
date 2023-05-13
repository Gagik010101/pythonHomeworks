list_str = []
len_str = []
with open("poem.txt", "r") as f:
    for i in f:
        sum = 0
        list_str = i.split()
        for n in list_str:
            sum = sum + len(n)
        len_str.append(sum)
f.close()
print(len_str)

