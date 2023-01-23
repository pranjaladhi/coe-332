#Pranjal Adhikari pa8729
import names

def nameLen(name): #function to determine length of full name
    return len(name) - 1

nameList = [] #generating an empty list

for i in range(5): #adding 5 total full names in the list
    nameList.append(names.get_full_name())

for n in range(5): #calling nameLen function and printing both full name and length of full name
    nlen = nameLen(nameList[n])
    print(nameList[n], nlen)
