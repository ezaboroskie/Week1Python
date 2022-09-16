number = int(input("Enter a Number: "))

check = False

if number < 0:
    print("Does not exist")
    
else:

    if number > 1:
        for x in range(2, number):
            if (number % x) == 0:
                check = True
                break

    if check:
        print(number, "is not a prime number")
    else:
        print(number, "is a prime number")