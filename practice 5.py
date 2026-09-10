Role= (input("Enter your role (Student/Teacher):"))
age =int(input("Enter your age:"))
eligible= Role=="Student" and age < 21
print("Eligible:",eligible)