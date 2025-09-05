with open("practice.txt","r+") as f:
    data = f.read()
    if(data.find("learning")!=-1):
        print("Found!! Learning is present")
    else:
        print("Not Found!!")
        
data = data.replace("Java","Python")
print(data)

with open("practice.txt","w") as f:
    f.write(data)

