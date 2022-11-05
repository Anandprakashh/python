test = input("Enter the name of the test: ")
mark = int(input("Enter the marks: "))
python = 100
java = 100
bash = 100
# if you want to change the test name later you can introduce the variable into constant 
if (test == "python" or "java" or "bash") and mark >= 90 and mark <= 100:
  print("A+ Grade")
elif (test == "python" or "java" or "bash") and mark >= 80 and mark <= 89:
  print("A Grade")
elif (test == "python" or "java" or "bash") and mark >= 70 and mark <= 79:
  print("B Grade")
elif (test == "python" or "java" or "bash") and mark >= 60 and mark <= 69:
  print("C Grade")
else:
  print("Not a considerable mark")
