print("Check If A Word Is A Palidrome")
while True:
    word = input("Enter a Word: ")
    
    if (word.casefold() == word[::-1].casefold()):
        print(f"{word} is a palindrome!")
    
    else:
        print(f"{word} is not a palindrome :(")
    
    quit = input("Press Enter to continue or q to quit: ")
    if quit.casefold() == "q".casefold():
        break