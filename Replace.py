def replace_word() :
    str = "Hello World! This is a Python Program made for replacing a word in a pre-defined string"
    qord = input("Enter the word to be replaced : ")
    nword = input("Enter the new word : ")     
    print(str.replace(qord, nword))

replace_word()