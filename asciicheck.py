alpha=input("Enter any letter: ")

if ord(alpha)>=65 and ord(alpha)<=90:
    print("Capital letter")


else: 
    if ord(alpha)>=97 and ord(alpha)<=122:
        print("Lower case")
    else:
        if ord(alpha)>=48 and ord(alpha)<=57:
            print("Digits")
        else:
            print("Any other character")