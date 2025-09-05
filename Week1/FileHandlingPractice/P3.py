def check_occurence():
    with open("practice.txt","r") as f:
        data1 = f.readline()
        data2 = f.readline()
        data3 = f.readline()
        data4 = f.readline()

    if data1.find("learning") != -1 :
        print("Line1")
    if data2.find("learning") != -1 :
        print("Line2")
    if data3.find("learning") != -1 :
        print("Line3")
    if data4.find("learning") != -1 :
        print("Line4")

check_occurence()