import sys
input = sys.stdin.readline

def checkAdd(n):
    sum = 0
    while n:
        sum += n.pop()  
    return list(map(int, str(sum)))

N = list(map(int, input().strip())) 

cnt = 0
while len(N) != 1:
    N = checkAdd(N)
    cnt += 1
print(cnt)

if N[0] % 3 == 0: print("YES")
else: print("NO")