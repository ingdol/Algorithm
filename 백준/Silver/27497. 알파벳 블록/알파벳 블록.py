from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
main_stack = deque()
history_stack = deque()
for _ in range(N):
    arr = input().split()
    if arr[0] == '1':
        main_stack.append(arr[1])
        history_stack.append(arr[0])
    elif arr[0] == '2':
        main_stack.appendleft(arr[1])
        history_stack.append(arr[0])
    else:
        if history_stack:
            s = history_stack.pop()
            if s == '1':
                main_stack.pop()
            elif s == '2':
                main_stack.popleft()

if main_stack: print(''.join(main_stack))
else: print(0)