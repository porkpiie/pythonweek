Timestable= int(input("Enter number you want the timestable of:"))
Range= int(input("Enter amount to multiply up to:"))


a=1


while a<=Range:
    print(Timestable, "x", a, "=",(Timestable*a))
    a=a+1