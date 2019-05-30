def countalpha (message, alpha):
    i = 0
    count = 0
    while i < len(message):
        if message[i].upper == alpha:
            count += 1
        i += 1
    if count > 0:
        print(alpha, "=", count)


msg=input("Enter any sentence: ")
c=65
while c<=90:
    countalpha(msg, chr(c))
    c += 1