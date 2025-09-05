print("Welcome to FIZZBUZZ Game!!")

def fb(r):
    for n in range(1,r):
        if(n%3==0 and n%5==0):
            print(" fizzbuzz"+"{"+str(n)+"}")
       
        if(n%3==0):
             print(" fizz"+"{"+str(n)+"}")
            
        if(n%5==0):
            print(" buzz"+"{"+str(n)+"}")
            
        if(n%3!=0 and n%5!=0):
            print(n)

fb(35)        

print("I hope you enjoyed FIZZBUZZ!!")

