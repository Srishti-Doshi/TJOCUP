import random

print("=================================================================================")
print("Welcome to THE WORDLE GAME!!")
print("=================================================================================")
print("""GAME RULES/GUIDELINES:
1. A random word will be selected and shown as underscores (_).
2. You can guess only one letter at a time.
3. If the letter is in the word, it will be revealed in the correct position(s).
4. If the letter is not in the word, you will lose 1 chance.
5. You have a total of 7 chances to guess the word.
6. If you guess all letters correctly before running out of chances, you win.
7. If you run out of chances before completing the word, you lose.
8. Repeating the same wrong letter will not reduce your chances again.""")
print("=================================================================================")
print("GOOD LUCK & HAVE FUN!")
print("=================================================================================")

WordList =["love", "time", "book", "moon", "star", "fire", "tree", "road", "rain", "wind", "gold", "song", "bird", "fish", "play", "ball", "king", "girl", "work", "code","ship", "land", "hope", "rock", "sand", "wave", "dark", "snow", "cold", "warm", "blue", "good", "fast", "slow", "high", "light", "heart", "water", "stone", "apple", "bread", "plant", "earth", "dream", "cloud", "sound", "music", "chair", "table", "river", "field", "grass", "house", "smile", "happy", "magic", "story", "peace", "clean", "sweet", "dance", "write", "think", "sleep", "green", "black", "white", "power", "laugh", "teach", "sunset", "forest", "castle", "friend", "school", "animal", "family", "garden", "winter", "summer","autumn", "spring", "flower", "planet", "silver", "little", "strong", "beauty", "wonder", "moment", "yellow", "orange", "purple", "bridge", "nature", "future", "memory", "spirit", "bright", "simple","gentle", "circle", "energy", "travel", "dreams"]

word = list(random.choice(WordList))
guess = []
chance = 7
wrongletter = []

for i in range(len(word)):
    guess.append("_")

print("Guess the Word: ",guess)

while(chance>0 and guess!=word):
    letter = input();

    if letter in wrongletter:
        print("Incorrect guess!!")
    
    if letter not in word:
        if letter not in wrongletter:
            chance = chance - 1
            print("Incorrect Guess!!\nChances left = ",chance)
            wrongletter.append(letter)
    if letter in word:
        for i in range(len(word)):
            if letter == word[i]:
                guess[i] = letter
        wrongletter.append(letter)
        print(guess)
        print("Correct guess!!\nChances left = ",chance)

if guess == word:
    print("You guessed it right!!\nWinner..")
else:
    print("OOPs you were unable to guess it , it was ",word)