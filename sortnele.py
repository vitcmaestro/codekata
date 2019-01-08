n = int(input(""))
li = list(map(int,input().split()))
for i in range(n):
    for j in range(i,n):
        if(li[i]>li[j]):
            li[i],li[j] = li[j],li[i]
for i in range(n):
    if(i != 0):
        print(" ",end = "")
    print(li[i],end = "")
