import random

randNum = random.randint(1,50)
print(randNum)

while True:
    userChoice = input("Guess the number From (1 to 100) or Quit(Q):")
    if (userChoice == "Q"):
        break
    
    userChoice = int(userChoice)
    if(userChoice == randNum):
        print("Success")
        break
    elif (userChoice > randNum):
        print("you number was greater")
    else:
        print("you number was small")
        
        
print("___Game Over____")
        
    