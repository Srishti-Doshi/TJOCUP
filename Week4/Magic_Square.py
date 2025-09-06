'''Magic Square: Hit and Trial

For example: size 3 
2 7 6
9 5 1
4 3 8
Steps:
1)In any magic square, 1 is located at position(n/2,n-1)
2)Let's the position of 1 is (p,q), then next number which is 2 is located at(p-1,q+1) position.
Anytime if calculated row position becomes -1 then make it n-1 and if column becomes n then make it 0.
3)If the calculated position already contains a number then decrement the column by 2 and increment the row by 1.
4)If anytime row position becomes -1 and column becomes n, switch it to(0,n-2).  '''

print("Welcome to Magic Square!!")
n = int(input("Enter size: "))

if n % 2 == 0:
    print("Oops! No magic square for even size like",n)
    exit()

print("Magic Square of size",n,":")
square = [[0 for j in range(n)]for i in range(n)]

for i in range(1,n*n+1):
    if i == 1:
        p = int(n/2); q = n-1
        square[p][q] = i
    else:
        p = p-1; q = q+1
        if p == -1 and q == n:
            p = 0
            q = n-2
        if p == -1:
            p = n-1
        if q == n:
            q = 0
        if square[p][q]!=0:
            p = p+1
            q = q-2
        square[p][q] = i

for i in range(n):
    for j in range(n):
        if(j==n-1):
            print(square[j][j])
        else:
            print(square[i][j],end = ",")
        
