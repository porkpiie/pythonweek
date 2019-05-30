file_read=open("data.txt", "r")
file_write=open("data2.txt", "w")
collector = []
a = input("Enter 1st letter to find and replace: ")
b = input("Ente 2nd letter to find and replace: ")

for char in file_read:
    if char == a:
        char = '*'
        print("*", file=file_write, end="")
    elif char == b:
        char = '*'
        print(ch, file=file_write, end=""
    collector.append(char)

new_string = ''.join(collector)