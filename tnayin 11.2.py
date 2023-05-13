def SumWords(Word):
    Sum = 0
    fileSum = open("file", "w")
    fileSum.write(Word)
    with open("file", "r") as fileSum:
        for i in fileSum:
            Words = i.split()
            for n in Words:
                Sum += 1
        return f"words in sentense = {Sum}"
    fileSum.close()


Word = input("input sentense")
print(SumWords(Word))
