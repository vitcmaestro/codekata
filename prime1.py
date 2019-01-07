import math
def isprime(num):
    if(num%2 == 0 or num == 1):
        return "no"
    for i in range(3,int(math.sqrt(num)+1)):
        if(num% i == 0):
            return "no"
    else:
        return "yes"

num = int(input(""))
print(isprime(num))
