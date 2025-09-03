import random
def evolve(data):
    index = random.randint(0,len(data)-1)
    p = random.randint(1,100)
    print(p)
    if(p==1):
        if(data[index]=='0'):
            data[index]=='1'
        else:
            data[index]=='0'

with open("dna_data.txt") as myfile:
    data=myfile.read()
    data = list(data)
for i in range(0,1000):
    evolve(data)
print(data)