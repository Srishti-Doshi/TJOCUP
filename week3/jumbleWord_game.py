# Jumbled Word Game!!
import random

def choose():
    words = ['rainbow','computer', 'srishti', 'puuung', 'player', 'mathematics', 'program', 'science', 'intelligent','Entertainment','cinema','nick','babysitter']
    pick = random.choice(words)
    return pick

def jumble(word):
    jumbled = "".join(random.sample(word, len(word)))
    return jumbled

def thank(p1n, p2n, p1, p2):
    print('\nFinal Scores:')
    print(p1n, ',Your score is : ',p1)
    print(p2n, ',Your score is: ',p2)
    
    if p1>=p2 :
        if p1 == p2 :
            print('Tie!!')
        else:
            print(p1n,'is Winner!!')
    else :
        print(p2n,'is Winner!!')
    print('Thanks for playing')
    
def play():
    p1name = input('Player 1, Please enter your name: ')
    p2name = input('player 2, Please enter your name: ')
    pp1 = 0
    pp2 = 0
    turn = 0
    
    while True:
        #Computer's Task
        picked_word = choose()
        
        #Create Question
        qn = jumble(picked_word)
        print("\nJumbled word is:", qn)
        
        #Player1
        if turn % 2 == 0 :
            print(p1name, 'Your Turn.')
            ans = input('What is on my mind? ')
            if ans == picked_word:
                pp1 = pp1 + 1
                print('Correct!! Your score is :',pp1)
            else:
                print('Better luck next time, I thought : ',picked_word)
                
            c = input('Press 1 to continue and 0 to quit: ')
            if int(c) == 0:
                thank(p1name,p2name,pp1,pp2)
                break
            turn = turn + 1
            
            #Player2
        else:
          print(p2name, 'Your Turn.')
          ans = input('What is on my mind? ')
          if ans == picked_word:
              pp2 = pp2 + 1
              print('Correct!! Your score is :',pp2)
          else:
              print('Better luck next time, I thought : ',picked_word)
                  
          c = input('Press 1 to continue and 0 to quit: ')
          if int(c) == 0:
             thank(p1name,p2name,pp1,pp2)
             break   
          turn = turn + 1
          
        
# Start the Game
play()
    