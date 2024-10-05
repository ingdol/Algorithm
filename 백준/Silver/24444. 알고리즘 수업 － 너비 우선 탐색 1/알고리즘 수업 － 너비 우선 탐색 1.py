import sys
input = sys.stdin.readline

def bfs(node):
    queue = [node]
    visited[node] = 1
    order_count = 2
    while queue:
        cur = queue.pop(0)
        for neighbor in graph[cur]:
            if visited[neighbor] == 0:
                queue.append(neighbor)
                visited[neighbor] = order_count
                order_count += 1

N, M, R = list(map(int, input().split()))
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    u, v = list(map(int, input().split()))
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, N + 1): 
    graph[i] = sorted(graph[i])

visited = [0]*(N+1)

bfs(R)

for i in range(1, N + 1):
    print(visited[i])