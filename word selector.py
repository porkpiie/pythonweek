msg=input("Enter any message")
what=input("what word are you looking for? ")

i=0
word=0

while i<len(msg):
    if msg[i] == " ":
        word=word+1

if what == word:
    print(word)
    
    i=i+1