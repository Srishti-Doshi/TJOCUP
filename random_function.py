import random
val = random.randint(1,5) # 1 and 5 included
print(val)

num = random.randrange(1,5) # 5 not included
print(num)

n = random.random()  # generates decimal number between 0 to 1
print(n)

even = random.randrange(2,10,2)
print(even)

odd = random.randrange(1,10,2)
print(odd)

numlist = random.choice([1,3,4,5,5])
print(numlist)