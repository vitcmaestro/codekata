val = input("")
test = val.lower()
if(test == 'a' or test == 'e' or test == 'i' or test == 'o' or test == 'u'):
    print("Vowel")
elif(ord(test)>=97 and ord(test)<=122):
    print("Consonant")
else:
    print("invalid")
