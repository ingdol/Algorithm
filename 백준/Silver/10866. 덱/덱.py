from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
dq = deque()
for _ in range(N):
    arr = input().split()
    command = arr[0]
    if command == 'push_front':
        dq.appendleft(arr[1])
    elif command == 'push_back':
        dq.append(arr[1])
    elif command == 'pop_front':
        if dq: print(dq.popleft())
        else: print(-1)
    elif command == 'pop_back':
        if dq: print(dq.pop())
        else: print(-1)
    elif command == 'size':
        print(len(dq))
    elif command == 'empty':
        if dq: print(0)
        else: print(1)
    elif command == 'front':
        if dq: print(dq[0])
        else: print(-1)
    elif command == 'back':
        if dq: print(dq[-1])
        else: print(-1)