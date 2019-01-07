import math
def isprime(num):
    if(num%2 == 0):
        return "yes"
    for i in range(3,int(math.sqrt(num))):
        if(num% i == 0):
            return "no"
    else:
        return "yes"

num = int(input(""))
print(isprime(num))
