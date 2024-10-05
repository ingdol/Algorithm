import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
person_1, person_2 = list(map(int, input().split()))
m = int(input())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    x, y = list(map(int, input().split()))
    graph[x].append(y)
    graph[y].append(x)

def bfs(start, target):
    visited = [False] * (n + 1)
    queue = deque([(start, 0)])

    visited[start] = True

    while queue:
        currunt, degree = queue.popleft()

        if currunt == target:
            return degree
        
        for neighbor in graph[currunt]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append((neighbor, degree + 1))
        
    return -1

result = bfs(person_1, person_2)
print(result)