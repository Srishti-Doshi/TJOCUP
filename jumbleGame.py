import random
#Jumble_word game
def choose():
    words = ["puung", "tinka","tiku", "sonu", "sahil","motu"]
    pick = random.choice(words)
    return pick

def jumble(word):
    jumbled = "".join(random.sample(word,len(word)))
    return jumbled

def thank(p1n, p2n,pp1, pp2):
    print("Final scores:")
    print(p1n,", Score: ",pp1)
    print(p2n,", Score: ",pp2)
    print("Thanks for playing!!")

def play():
    print("Welcome to 2 players game , Jumble Word!!")
    p1n = input("Player 1, please enter your name: ")
    p2n = input("Player 2, please enter your name: ")
    pp1 = 0
    pp2 = 0
    turn = 0
    
    while True:
        #Computer's task
        picked_word = choose()
        qn = jumble(picked_word)
        print("Jumbled word: ",qn)
        
        if turn % 2 == 0:
            print(p1n,"your turn")
            answer = input("What's in your mind? ")
            if answer == picked_word:
                print("You guessed it right!!")
                pp1 += 1 
            else:
                print("Better luck next time!! , Right word is ",picked_word)
            
            turn += 1 
            
        else:
            print(p2n,"your turn")
            answer = input("What's in your mind? ")
            if answer == picked_word:
                print("You guessed it right!!")
                pp2 += 1 
            else:
                print("Better luck next time!! , Right word is ",picked_word)
            
            turn += 1 
            
        exit = input("Enter 0 to exit: ")
        if int(exit) == 0:
            thank(p1n, p2n, pp1, pp2)
            break
        
#Start
play()
    
     
     
        