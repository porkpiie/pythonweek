T=input("Enter Today's temp:")
Temp = int(T)
if Temp>30:
    print("Hot, might be too hot, might be...")
if Temp in range (16,30):
    print("Still hot, slightly less so")
if Temp<=15:
    print("Just right.. :)")
