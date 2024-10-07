import sys
input = sys.stdin.readline
from collections import deque

def bfs(R):
    queue = deque([R])
    visited[R] = 1
    cnt = 1
    while queue:
        node = queue.popleft()
        for inner_node in graph[node]:
            if visited[inner_node] == 0:
                cnt += 1
                visited[inner_node] = cnt
                queue.append(inner_node)

N, M, R = map(int, input().split())

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, N + 1):
    graph[i].sort()
    
visited = [0 for _ in range(N + 1)]
bfs(R)

for i in range(1, N + 1):
    print(visited[i])