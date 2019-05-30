def reverseWordSentence(Sentence): 
    words = Sentence.split(" ") 
    newWords = [word[::-1] for word in words] 
    newSentence = " ".join(newWords) 
    return newSentence 
  
 
Sentence =input("Enter any sentence: ")


print(reverseWordSentence(Sentence)) 