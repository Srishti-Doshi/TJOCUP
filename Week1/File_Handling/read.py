file = open("file.txt", "r")

data = file.read(3)
print(data)

print(type(data))

data1 = file.read()
print(data1)

file.close()
