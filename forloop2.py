def reverse(word):
    newword=""
    i=len(word)-1
    while i>=0:
        newword += word[i]
        i -= 1
    return newword


message=input("Enter any sentence: ")
newmessage = ""
word = ""
i = 0

while i < len(message):
    if message[i] == " ":
        newmessage += reverse(word) + " "
        word = ""
    else:
        word += message [i]
    i = i+1

print(newmessage,reverse(word))