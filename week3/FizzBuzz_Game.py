print("Welcome to FIZZBUZZ Game!!")
play = 1

while(play == 1):
    n = int(input("Enter a number: "))
    if(n%3==0 and n%5==0):
        print("fizzbuzz")
        
    if(n%3==0 and n%5!=0):
        print("fizz")
        
    if(n%3!=0 and n%5==0):
        print("buzz")
        
    if(n%3!=0 and n%5!=0):
        print(n)
    play = int(input("Do you want to play FIZZBUZZ again?\n(Enter 1 to play and 0 to exit):" ))

print("I hope you enjoyed FIZZBUZZ!!")