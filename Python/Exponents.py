def exponent(x , y):
  result=1
  for index in range (1, y+1):
      result = result * x
  return result

x=int(input("Enter the base number: "))
y=int(input("Enter the exponent number: "))

print(exponent(x , y))