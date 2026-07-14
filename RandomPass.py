
# import random
# import string

# pwd = (string.ascii_letters + string.ascii_letters )
# randPwd = "".join( random.choices(pwd, k=8))
# print(randPwd)

#!/bin/python3

# import math
# import os
# import random
# import re
# import sys


# if __name__ == '__main__':
#     n = int(input().strip())

    
    
# for i in range(1, int(input())):  # Already provided by the challenge
#     print(i * (10**i - 1) // 9)
    
# for i in range(1, int(input()) + 1): print(((10**i - 1) // 9) ** 2)
  
    
# How the Math Works:(10i - 1) // 9: This creates a number consisting entirely of 1s based on the row i.If $i = 1 \implies (10 - 1) // 9 = 1$If $i = 2 \implies (100 - 1) // 9 = 11$If $i = 3 \implies (1000 - 1) // 9 = 111$i * ...: Multiplying that sequence of 1s by i transforms it into the repeating digit for that row.Row 1: $1 \times 1 = 1$Row 2: $2 \times 11 = 22$Row 3: $3 \times 111 = 333$Row 4: $4 \times 1111 = 4444$

    
def fizzbuz(n):
    for i in range(1,n+1):
        if i % 15 == 0:
            print("FizzBuzz")
        elif i % 3 == 0 :
            print("Fizz")
        elif i % 5 == 0:
            print ("Buzz")
        else:
            print(i)

print(fizzbuz(15))

# n = int(input())  # Reads how high you want to count

# for i in range(1, n + 1):
#     if i % 15 == 0:
#         print("fizzbuzz")
#     elif i % 3 == 0:
#         print("fizz")
#     elif i % 5 == 0:
#         print("buzz")
#     else:
        # print(i)