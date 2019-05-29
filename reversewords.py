def reverseWordSentence(Sentence): 

	 
	words = Sentence.split(" ") 
	# Reversing each word and creating 
	# a new list of words 
	# List Comprehension Technique 
	newWords = [word[::-1] for word in words] 
	
	# Joining the new list of words 
	# to for a new Sentence 
	newSentence = " ".join(newWords) 

	return newSentence 

# Driver's Code 
Sentence = "GeeksforGeeks is good to learn"
# Calling the reverseWordSentence 
# Function to get the newSentence 
print(reverseWordSentence(Sentence)) 
