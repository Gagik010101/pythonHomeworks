def sentense_wordsl_ess_thanor_equal_to_4(sentense):
    File = open("textfile.txt", "w")
    File.write(sentense)
    with open("textfile.txt", "r") as File:
        for i in File:
            Wordslist = i.split()
            for word in Wordslist:
                if len(word) < 4:
                    print(word)
    File.close()
    return "Function END"





sentense = input("input sentense")
print(sentense_wordsl_ess_thanor_equal_to_4(sentense))