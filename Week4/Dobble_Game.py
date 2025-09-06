'''Dobble Game - Spot the similarity
The person should see two lists, the lists should have only one common letter,
The person should tell which letter is common in both.'''

import random
print("Welcome to Dobble Game!!")

str1 = random.choice(["AEIMQ","BFJNQ","GKOQ","DHLPQ","AFKPR","BELOR","CHINR","DGJMR","AGLNS","BHKMS","CEJPS","DFIOS","AHJOT","BGIPT","CFLMT","DEKNT","ABCDU","EFGHU","IJKLU","MNOPU"])
str2 = random.choice(["AEIMQ","BFJNQ","GKOQ","DHLPQ","AFKPR","BELOR","CHINR","DGJMR","AGLNS","BHKMS","CEJPS","DFIOS","AHJOT","BGIPT","CFLMT","DEKNT","ABCDU","EFGHU","IJKLU","MNOPU"])

print("List 1:",str1)
print("List 2:",str2)

answer = input("You have to find that which letter is common in both the above lists ")

for i in str1:
    for j in str2:
        if i == j:
            letter = i

if answer == letter:
    print("Correct!!")
else:
    print("Nope!!")
    print("The correct common letter is ",letter)

