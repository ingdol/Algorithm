import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().strip())) for _ in range(N)]

res = []

def recursion(n, x, y):
    total = 0
    for i in range(n):
        for j in range(n):
            total += arr[x + i][y + j]
    
    if total == 0:
        res.append("0")
    elif total == n * n:
        res.append("1")
    else:
        n //= 2
        res.append("(")
        recursion(n, x, y)
        recursion(n, x, y + n)
        recursion(n, x + n, y)
        recursion(n, x + n, y + n)
        res.append(")")

recursion(N, 0, 0)
print("".join(res))