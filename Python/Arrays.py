friends = ["Mark", "Alex", "Carol", "Neil", "Caroline"]

#goes through a range in an array (start to end -1)
for index in range (0, len(friends)):
    print(friends[index])

#goes through every element of the array
for friend in friends:
    print(friend)

#goes through the entire length of array skipping 1 (pass 2)
for index in range(0, len(friends),2):
    print(friends[index])

#runs a loop in reverse order
for index in range(len(friends) - 1, -1, -1):
    print(friends[index])