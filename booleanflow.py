no=int(input("Enter any number"))
if no>1000:
    print("Great")
    if no>2000:
        print("Greater")
    else:
        print("Greatish")
    print("2")    
else:
    print("Trash")
    if no>500:
        print("Not as Trash")
    else:
        print("Not the most Trash")
    print("1")