a = list(map(int,input().split()))
max = 0
for i in range(3):
    if(max< a[i]):
        max = a[i]
print(max)
