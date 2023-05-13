import string
def function(SENTENCE, kay):
    h = None
    u = 0
    simbols = list(string.printable)
    L = SENTENCE.split()
    dec = []
    for i in L:
        g = str()
        for n in i:
            if n in simbols:
                s = simbols.index(n)
                if W == 1:
                    s = s - len(simbols)
                    s = kay + s
                else:
                    s = s - kay
                h = simbols[s]
                g = g + h
        dec.append(g)
    for k in dec:
        print(k, end=" ")

W = int(input("input number 1 for Encoding\ninput number 2 for Decoding\nimput number:\t"))
if W == 1:
    SENTENCE = str(input('input text for Encoding\t'))
else:
    SENTENCE = str(input('input text for Decoding\t'))
kay = int(input('input number\t'))
while kay > 100:
    kay = int(input("plese enter a number less than 100:\t"))
function(SENTENCE, kay)
