import sys
input = sys.stdin.readline

N = int(input())
list = []

for _ in range(N):
    list.append(int(input().strip()))

a = list[-1]
cnt = 1
list.reverse()
for n in list:
    if n <= a:
        continue
    else: 
        cnt += 1
        a = n
print(cnt)