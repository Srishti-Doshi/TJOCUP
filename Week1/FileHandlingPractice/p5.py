with open("numbers.txt","w") as f:
    f.write("11,11,2,12")

with open("numbers.txt","r") as f:
    data = f.read()
    even = 0
    Number_list = []
    num = ""
    for i in range(len(data)):
        if data[i]==",":
           Number_list.append(int(num))
           num = ""
        else:
            num += data[i]
        if num != "":
            Number_list.append(int(num))

    for i in Number_list:
        if(i % 2 == 0):
            even += 1
        
print(even)