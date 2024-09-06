import sys
input = sys.stdin.readline

N = int(input())
dic = {}

for _ in range(N):
    [S, X] = input().split()
    X = int(X)
    if S in dic:
        dic[S] += X
    else: dic[S] = X
    
if 5 in dic.values():
    print('YES')
else: print('NO')