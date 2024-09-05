N = int(input())
arr = [[" " for _ in range(4 * N - 3)] for _ in range(4 * N - 3)]

def star(n, x, y):
    if n == 1:
        arr[y][x] = "*"
        return

    len = 4 * n - 3

    for i in range(len):
        arr[y][x + i] = "*"
        arr[y + i][x] = "*"
        arr[y + len - 1][x + i] = "*"
        arr[y + i][x + len - 1] = "*"

    star(n - 1, x + 2, y + 2)

star(N, 0, 0)
for s in arr:
    print("".join(s))