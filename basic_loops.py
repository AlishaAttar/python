correct_pass="Some_pass"
not_found=True
while not_found:
    passw= input("Enter your password")
    if passw== correct_pass:
          not_found = False
          print("Password matched")