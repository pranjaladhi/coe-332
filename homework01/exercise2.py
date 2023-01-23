#Pranjal Adhikari pa8729
import names

i = 0

while (i < 5): #taking a 5 random full names from names library and printing only
    name = names.get_full_name() #if number of characters equal 8
    if len(name) == 9:
        print(name)
        i = i + 1
