from collections import defaultdict
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
adj_list = [[] for _ in range(N + 1)]

for _ in range(M):
    u, v = map(int, input().split())
    adj_list[u].append(v)
    adj_list[v].append(u)

visited = [False for _ in range(N + 1)]

def bfs(node):
    visited[node] = True
    queue = [node]

    while queue:
        cur_node = queue.pop(0)
        for neighbor in adj_list[cur_node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
                
result = 0
for node in range(1, N + 1):
    if not visited[node]:
        bfs(node)
        result += 1
print(result)