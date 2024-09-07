import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

res = []

for i in range(N):
    res.insert(i-arr[i], i+1)

for n in res:
    print(n, end=' ')