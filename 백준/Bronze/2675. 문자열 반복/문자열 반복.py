import sys
input = sys.stdin.readline

N = int(input())

for _ in range(N):
    P = ''
    arr = input().split()
    R = int(arr[0])
    S = arr[1]

    for s in S:
        P += s*R
    
    print(P)