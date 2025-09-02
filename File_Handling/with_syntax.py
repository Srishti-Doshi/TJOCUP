with open("demo.txt","r") as f:
    print(f.read())

with open("demo.txt","r+") as f:
    f.write("Hello")
    