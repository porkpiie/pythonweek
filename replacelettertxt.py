file_read=open("data.txt", "r")
file_write=open("data2.txt", "w")

for data in file_read:
    for ch in data:
        if ch == "a":
            print("*", file=file_write, end="")
        elif ch == "s":
            print("*", file=file_write, end="")
        else:
            print(ch, file=file_write, end="")
