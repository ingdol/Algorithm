import sys
input = sys.stdin.readline

Acnt, Bcnt = list(map(int, input().split()))

A = set(map(int, input().split()))
B = set(map(int, input().split()))

cnt = Acnt + Bcnt

for b in list(B):
    if b in A:
        cnt -= 1

for a in list(A):
    if a in B:
        cnt -= 1
print(cnt)