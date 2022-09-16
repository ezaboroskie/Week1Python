def perfectSquares(x, y):
    lists=[]
    for index in range (x, y + 1):
        n=1
        while n*n <= index:
            if n*n == index:
                lists.append(index)
            n=n+1
        index = index + 1
    return len(lists)

x=int(input("Enter the starting range: "))
y=int(input("Enter the ending range: "))

print("Number of perfect squares between range is: ", perfectSquares(x, y))