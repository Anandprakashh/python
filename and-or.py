#or 	will give you the first value if it is true otherwise it will give you the second value.
name = input("Enter your name: ")
surename = input("Enter your surename: ")
result = name or f"Mr {surename}"
print(result)

#and  will give you the first value if it is false otherwise it will give you the second value.
name = input("Enter your name: ")
surename = input("Enter your surename: ")
result = name and f"Mr {surename}"
print(result)
