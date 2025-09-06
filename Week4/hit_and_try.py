def generate_magic_square(n):
    if n % 2 == 0:
        print("Magic square works only for odd numbers here!")
        return

    magic_square = [[0] * n for _ in range(n)]

    i, j = 0, n // 2 
    num = 1

    while num <= n * n:
        magic_square[i][j] = num
        num += 1

        new_i, new_j = (i - 1) % n, (j + 1) % n

        if magic_square[new_i][new_j]: 
            i = (i + 1) % n
        else:
            i, j = new_i, new_j

    for row in magic_square:
        print(" ".join(str(x).rjust(2) for x in row))

generate_magic_square(3)
