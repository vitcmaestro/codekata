n = int(input(""))
li = list(map(int,input().split()))
miner = li[0]
for i in range(1,n):
    if(li[i]<miner):
        miner = li[i]
print(miner)
