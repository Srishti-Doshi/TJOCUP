'''Dobble Game - Spot the similarity
The person should see two lists, the lists should have only one common letter,
The person should tell which letter is common in both.'''

import random
print("Welcome to Dobble Game!!")
n = int(input("Select Difficult Level(5-10): "))

AlphabetList = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
#list1 = random.choice(["AEIMQ","BFJNQ","GKOQ","DHLPQ","AFKPR","BELOR","CHINR","DGJMR","AGLNS","BHKMS","CEJPS","DFIOS","AHJOT","BGIPT","CFLMT","DEKNT","ABCDU","EFGHU","IJKLU","MNOPU"])
#list2 = random.choice(["AEIMQ","BFJNQ","GKOQ","DHLPQ","AFKPR","BELOR","CHINR","DGJMR","AGLNS","BHKMS","CEJPS","DFIOS","AHJOT","BGIPT","CFLMT","DEKNT","ABCDU","EFGHU","IJKLU","MNOPU"])

def selectlist(AlphabetList,n):
    common = random.choice(AlphabetList)
    list1 = [common]
    list2 = [common]
    letter = ''

    while len(list1)<n:
        letter = random.choice(AlphabetList)
        if letter not in list1:
            list1.append(letter)

    while len(list2)<n:
        letter = random.choice(AlphabetList)
        if letter not in list1 and letter not in list2:
            list2.append(letter)
        
    random.shuffle(list1)
    random.shuffle(list2)

    return list1,list2,common
   
list1,list2,common=selectlist(AlphabetList,n)

print("List 1:",list1)
print("List 2:",list2)


answer = input("You have to find that which letter is common in both the above lists: ")

if answer == common:
    print("Correct!!")
else:
    print("Nope!!")
    print("The correct common letter is ",common)

