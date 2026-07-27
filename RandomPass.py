import random
import string

while True:
    length = int(input("Enter Password length: "))
    char = (string.ascii_letters + string.ascii_letters + string.punctuation)
    
    try:
        if length < 6:
            print("Password length must be at least 6..")
            continue
    except ValueError:
        print("Invalid input! Please Enter a Number.")
        continue   
         
    
    pwd = ""
    for i in range(length):
        pwd += random.choice(char)
    
    print(f"You Password is: {pwd}")
    
    userchoice = input("Do you want another Password? (y/n):")
    if userchoice.lower() !='y':
        print("Bye!...")
        break
    
    
