import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(node, order):
    visited[node] = order
    order_count[0] += 1
    
    for neighbor in graph[node]:
        if visited[neighbor] == 0:
            dfs(neighbor, order_count[0])

N, M, R = list(map(int, input().split()))
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    u, v = list(map(int, input().split()))
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, N + 1):
    graph[i] = sorted(graph[i])

visited = [0]*(N+1)
order_count = [1]

dfs(R, 1)

for i in range(1, N + 1):
    print(visited[i])