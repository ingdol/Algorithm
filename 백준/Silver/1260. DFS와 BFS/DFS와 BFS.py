import sys
input = sys.stdin.readline

def dfs(c):
    ans_dfs.append(c)
    visited[c] = 1

    for n in adj[c]:
        if not visited[n]:
            dfs(n)

def bfs(start):
    queue = []
    queue.append(start)
    ans_bfs.append(start)
    visited[start] = 1

    while queue:
        c = queue.pop(0)
        for n in adj[c]:
            if not visited[n]:
                queue.append(n)
                ans_bfs.append(n)
                visited[n] = 1

N, M, V = map(int, input().split())

adj = [[] for _ in range(N+1)]
for _ in range(M):
    start, end = map(int, input().split())
    adj[start].append(end)
    adj[end].append(start)

for i in range(1, N+1):
    adj[i].sort()

visited = [0]*(N+1)
ans_dfs = []
dfs(V)

visited = [0]*(N+1)
ans_bfs = []
bfs(V)

print(*ans_dfs)
print(*ans_bfs)