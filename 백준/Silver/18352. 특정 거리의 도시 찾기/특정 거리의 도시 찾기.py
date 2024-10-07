import sys
input = sys.stdin.readline
from collections import deque

N, M, K, X = map(int, input().split())

def bfs(x):
    queue = deque([x])
    visited[x] = 1

    while queue:
        stand_node = queue.popleft()
        plus_distance = visited[stand_node]

        for inner_node in graph[stand_node]:
            if visited[inner_node] == 0:
                visited[inner_node] = plus_distance + 1
                queue.append(inner_node)

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)

visited = [0 for _ in range(N + 1)]
bfs(X)

result = []
for i in range(1, N + 1):
    if K == visited[i] - 1:
        result.append(i)

if result: print(*result, sep='\n')
else: print(-1)