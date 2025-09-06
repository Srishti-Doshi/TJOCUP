n = int(input())

list1 = []
list2 = []
list3 = []

for i in range(n):
    list1.append([])
    list2.append([])
    list3.append([0 for i in range(n)])

for i in range(n):
    list1[i]= input().split(",")

for i in range(n):
    list2[i]= input().split(",")

for i in range(n):
    for j in range(n):
        list1[i][j]= int(list1[i][j])
        list2[i][j]= int(list2[i][j])

for i in range(n):
    for j in range(n):
        for k in range(n):
            list3[i][j] += list1[i][k]*list2[k][j]


for i in range(n):
    for j in range(n):
        if(j!=n-1):
            print(list3[i][j],end=",")
        else:
            print(list3[i][j],"")
