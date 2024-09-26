from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
queue = deque()
for _ in range(N):
    arr = input().split()
    command = arr[0]
    if command == 'push':
        queue.append(arr[1])
    elif command == 'pop':
        if queue: print(queue.popleft())
        else: print(-1)
    elif command == 'size':
        print(len(queue))
    elif command == 'empty':
        if queue: print(0)
        else: print(1)
    elif command == 'front':
        if queue: print(queue[0])
        else: print(-1)
    elif command == 'back':
        if queue: print(queue[-1])
        else: print(-1)