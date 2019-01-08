n = int(input(""))
arr = list(map(int,input().split()))
arr.sort()
if(n%2 != 0):
    s = n//2
    print(arr[s])
else:
    s = n//2
    av = (arr[s]+arr[s+1])/2
    print(av)
