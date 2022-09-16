
def factorial(number):
    result=1
    for index in range(1, number+1):
        result *= index
    return result 
    

number = int(input("Please Enter a Number: "))

if number < 0:
    print("Factorial of that number does not exist.")

elif number == 1:
    print(1)

else:
    result = factorial(number)
    print(result)


