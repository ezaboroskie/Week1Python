#Empty Dictionary 
#name = {}
user={}

name={}

firstName=input("Enter First Name: ")
lastName=input("Enter Last Name: ")

name["first_name"] = firstName
name["last_name"] = lastName

print("My name is" , name["last_name"] , "," , name["first_name"])


address1={"street": "3200 Maple Rd" , "city": "Atlanta" , "state": "Georgia", "zip-code":"30274"}
address2={"street": "485 Bridge St", "city": "Richmond", "state": "Virginia", "zip-code": "49314"}


user["addresses"]= [address1, address2]


print(user)
