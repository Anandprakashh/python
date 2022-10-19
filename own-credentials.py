print("Secure Login!")
print()
user_name = input("Username: ")
password = input("Password: ")
if user_name == "anand" and password == "password":
  print("Welcome Anand!")
elif user_name == "chris" and password == "password1":
  print("Hello Chris!")
elif user_name == "john" and password == "password2":
  print("Hi John!")
else:
  print("Access Denied")
