def change(message):
    i=0
    newmessage =""
    while i < len(message):
        asc=ord(message[i])
        if asc>=65 and asc<=90:
            newmessage += chr(asc+32)
        elif asc>=97 and asc<=122:
            newmessage += chr(asc-32)
        elif asc>=48 and asc <=57:
                newmessage += str(int(chr(asc))*2)
        else:
                newmessage += chr(asc)
        i += 1
    return newmessage                    


msg=input("Enter any message: ")
print(change(msg))