#Pranjal Adhikari pa8729
wordsList = [] #generating empty list

with open('words', 'r') as w: #opening, reading, and adding words into wordsList
    wordsList = w.read().splitlines()

wordsList.sort(key = len, reverse = True) #sorting wordsList in length descending order 

for i in range(5): #printing 5 longest words in wordsList
    print(wordsList[i])

