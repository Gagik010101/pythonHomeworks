Python = open("python.txt", "w")
word = input("input sentense\t")
Python.write(word)
Python.close()
Python = open("python.txt", "r")
print(Python.read())

