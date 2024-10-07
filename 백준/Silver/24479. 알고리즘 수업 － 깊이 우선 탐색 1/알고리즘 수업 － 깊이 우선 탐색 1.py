import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(R, cnt):
    visited[R] = cnt
    order_count[0] += 1
    for inner_node in graph[R]:
        if visited[inner_node] == 0:
            dfs(inner_node, order_count[0])

N, M, R = map(int, input().split())

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, N + 1):
    graph[i].sort()

visited = [0 for _ in range(N + 1)]
order_count = [1]
dfs(R, 1)

for i in range(1, N + 1):
    print(visited[i])