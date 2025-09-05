word = "learning"

def check_word():
    with open("practice.txt","r") as f:
        data = f.read()
        if(word in data):
            print("found")
        else:
            print("not found")


def check_in_line():
    line_no=1
    data = True
    with open("practice.txt","r") as f:
        while data:
            data = f.readline()
            if(word in data):
                print(line_no)
                return
            line_no += 1
    return -1

check_word()
print(check_in_line())