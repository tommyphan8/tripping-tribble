LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

letterCount = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0,
'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0,
'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0}

wordCount = {"THE": 0, "WHEN": 0}

#message = "Mark Antony's was by Caesar. He chid the sisters"
message = "asd Hello Hello asdfg wqert asdf"
message = message.replace("-", "")

largestWord = []

#counts the the letter frequency 
#@message - string that the function will count
#@letterCount - array that stores the frequency of each letter
def getLetterCount(message, letterCount):
	for letter in message.upper():
		if letter in LETTERS:
			letterCount[letter] += 1
	print(letterCount)		


#counts the word frequency
#@message - string that the function will parse and count
#@
def getWordCount(message, wordCount):
	wordArray = message.upper().split()
	for word in wordArray:
		if word == "THE":
			wordCount[word] +=1
		elif word == "WHEN":
			wordCount[word] += 1
	print (wordCount)


def getBiggestWord(message, largestWord):
	wordArray = message.upper().split()
	for word in wordArray:
		if not largestWord:
			largestWord.append(word)
		elif len(word) == len(largestWord[0]) and word != largestWord[0]:
			largestWord.append(word)
		elif len(word) > len(largestWord[0]):
			del largestWord[:]
			largestWord.append(word)
	print largestWord
			

print message
getBiggestWord(message, largestWord)
getWordCount(message, wordCount)
getLetterCount(message, letterCount)
