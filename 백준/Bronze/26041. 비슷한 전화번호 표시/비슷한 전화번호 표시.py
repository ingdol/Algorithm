import sys
input = sys.stdin.readline

A = list(input().split())
B = input().strip()
cnt = 0
for a in A:
    if a.startswith(B) and a != B:
        cnt += 1

print(cnt)