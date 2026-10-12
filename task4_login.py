email = input("Enter your email: ")
password = input("Enter your password: ")

correct_email = "abc@gmail.com"
correct_password = "abc"

if email == correct_email and password == correct_password:
    print("User is logged in")
elif email == correct_email:
    print("Password is not correct")
elif password == correct_password:
    print("Please enter the correct email")
else:
    print("Both email and password are incorrect")
