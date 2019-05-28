f=0
msg=input("Enter any message: ")
find=input("what word are you looking for? ")


i=0


while i<len(msg):
    if msg[i] == find[0]:
        if msg[i:i+len(find)] == find:
            f=f+1
            i=i+len(find)-1
    i=i+1


print("There are", f, find,"(s)")