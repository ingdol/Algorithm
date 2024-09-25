import sys
input = sys.stdin.readline

N = int(input())
res = 0
for _ in range(N):
    str = input().split()[0]
    stack = [str[0]]
    for i in range(1, len(str)):
        if stack:
            if stack[-1] == str[i]:
                stack.pop() 
            else: stack.append(str[i])
        else: stack.append(str[i])
    if not len(stack): res += 1
    
print(res)
