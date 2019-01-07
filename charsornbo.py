victim = input("")
try:
    test = ord(victim.lower())
    if(test>=97 and test<=122):
        print("Alphabet")
except:
    print("No")
