import math

def isprime(val):
    if(val%2 == 0):
        return False
    else:
        for i in range(3,int(math.sqrt(val))+1):
            if(val%i == 0):
                return False
        else:
            return True
            
a,b = map(int,input().split())
c = 0
for i in range(a,b):
    if(isprime(i)):
        if(c!=0):
            print(" ",end="")
        print(i,end="")
        c+=1
                
