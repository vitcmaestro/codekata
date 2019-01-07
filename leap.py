year = int(input(""))
if(year %4 == 0):
    if(year%100 !=0):
        print("yes")
    elif(year%400 == 0):
        print("yes")
    else:
        print("no")
else:
    print("no")
