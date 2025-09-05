Shopping = ["Curd","Apple","Soap"]
print(Shopping)

for item in Shopping:
    print(item)
    
Shopping.append("Cashew")
print(Shopping)

print(Shopping[0])

Shopping.insert(1,"Potatoe")

for i in range(5):
    print(Shopping[i])
    
AgeList = [24,12,21,21,18,19,45,34,55,18]
print(AgeList.count(18))

print("Length is ",len(AgeList))

for i in range(len(Shopping)):
    print(Shopping[i])
    
print(len(Shopping))

print(AgeList)
AgeList.sort()
print(AgeList)
AgeList.reverse()
print(AgeList)
AgeList.reverse()
print(AgeList)

Names = ["Srishti", "Prince", "Sanidhya", "Sangita"," Gajanand", "Motu"]
print(Names)
Names.sort()
print(Names)
Names.reverse()
print(Names)

Names.insert(0,"Baby")
print(Names)



