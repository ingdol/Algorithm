import sys
input = sys.stdin.readline

N = int(input())
res = 0

for _ in range(N):
    word = input().strip()
    stack = []
    for char in word:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)
    if not stack:
        res += 1

print(res)