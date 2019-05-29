from collections import Counter
word = input("Enter a word")

Alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    
counts=Counter(word)
for i in word:
    print(i,counts[i])

