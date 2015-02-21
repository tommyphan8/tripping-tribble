import sys
import os
import matplotlib.pyplot as plt
import numpy

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

#set that stores frequency of letters"
letterCount = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0,
'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0,
'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0}


#set that stores frequency of words: "the" and "when"
wordCount = {"THE": 0, "WHEN": 0}

#list that stores largest word
largestWord = []

#counts the the letter frequency 
#@message - string that the function will count
#@letterCount - set that stores the frequency of each letter
def getLetterCount(message, letterCount):
	for letter in message.upper():
		if letter in LETTERS:
			letterCount[letter] += 1
	#print(letterCount)		


#counts the word frequency
#@message - string that the function will parse and count
#@wordCount - set that stores frequency of words
def getWordCount(message, wordCount):
	wordArray = message.upper().split()
	for word in wordArray:
		if word == "THE":
			wordCount[word] +=1
		elif word == "WHEN":
			wordCount[word] += 1
	#print (wordCount)

#checks if 
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
	#print largestWord

def main(file, LETTERS, letterCount, wordCount, largestWord):

	#Check if file exists	
	if not os.path.exists(file):
		print("Error: " + file + " does not exists")
		exit(1)
	
	#Open file for reading
	fi = open(file, "r")

	for line in fi:
		message = line		
		message = message.replace("-", "")
		getBiggestWord(message, largestWord)
		getWordCount(message, wordCount)
		getLetterCount(message, letterCount)
	fi.close()
						
	print largestWord
	print wordCount
	print letterCount
	print("Completed Successfully")


if __name__ == "__main__":
    # Check number of command line arguments and call CommentOut function
    if len(sys.argv) == 2:
	main(sys.argv[1], LETTERS, letterCount, wordCount, largestWord)       
        exit(0)
    print("Usage: " + sys.argv[0] + " <file>")
    exit(1)
