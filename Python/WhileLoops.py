#while conditions are infinite loops until condition is met

#infinite loop
#while True:
    #print("Hello World!")

counter = 0

while counter < 10:
    print("Hello!")
    counter += 1 #increment of 1

while health > 0:
    print ("Continue the game!")
    print ("Player dies!")
    health = 0

while True:
    friend_name = input("Enter your friend name")
    print(friend_name)
    choice = input("Enter q to quit or any key to continue!")
    if choice == "q":
        break  #stops loop
