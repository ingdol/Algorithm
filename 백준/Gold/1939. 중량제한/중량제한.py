import sys
input = sys.stdin.readline
from collections import deque

def bfs(mid):
    queue = deque([start])
    visited = [0 for _ in range(N + 1)]
    visited[start] = 1

    while queue:
        cur_node = queue.popleft()
        if cur_node == end:
            return True
        for next_node, weight in graph[cur_node]:
            if visited[next_node] == 0 and weight >= mid:
                visited[next_node] = 1
                queue.append(next_node)

N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]
for _ in range(M):
    A, B, C = map(int, input().split())
    graph[A].append((B, C))
    graph[B].append((A, C))

for i in range(1, N + 1):
    graph[i] = sorted(graph[i], key= lambda item : item[1], reverse=True)

start, end = list(map(int, input().split()))

low, high = 1, 1000000000
answer = low

while low <= high:
    mid = (low + high) // 2
    if(bfs(mid)):
        answer = mid
        low = mid + 1
    else: 
        high = mid - 1

print(answer)