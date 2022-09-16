while True:
    word = input("Enter a word: ")

    if (word.casefold() == word[::-1].casefold()):
        print(f"{word} is a palidrome")
    else:
        print(f"{word} is not a palidrome")