h1,m1 = map(int,input().split())
h2,m2 = map(int,input().split())
if(h1>=h2):
    hans = h1-h2
    if(m1>=m2):
        mans = m1-m2
    else:
        hans = hans-1
        mans =  (m1+60)-m2

else:
    hans = h2-h1
    if(m2>=m1):
        mans = m2-m1
    else:
        hans = hans-1
        mans =  (m2+60)-m1

print(hans,mans)  
