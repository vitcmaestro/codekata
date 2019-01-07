lim,k = map(int,input().split())
lis = list(map(int,input().split()))
sum = 0
for i in range(k):
    sum = sum+lis[i]
print(sum)
