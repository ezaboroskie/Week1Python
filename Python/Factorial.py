while True:
    number = int(input("Enter a Number: "))
    factorial = 1
    if number < 0: 
        print ("A factorial does not exist for this number")
    else:
        for n in range (1, number + 1):
            factorial = factorial*n
        print("The factorial of", number, "is", factorial)

