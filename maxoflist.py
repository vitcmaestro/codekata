n = int(input(""))
li = list(map(int,input().split()))
maxer = 0
for i in range(n):
    if(li[i]>maxer):
        maxer = li[i]
print(maxer)
