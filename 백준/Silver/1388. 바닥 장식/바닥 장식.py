import sys
input = sys.stdin.readline

def dfs(x, y):
    visited[x][y] = True

    if floor[x][y] == '-':
        if y + 1 < M and not visited[x][y + 1] and floor[x][y + 1] == '-':
            dfs(x, y + 1)
    
    elif floor[x][y] == '|':
        if x + 1 < N and not visited[x + 1][y] and floor[x + 1][y] == '|':
            dfs(x + 1, y)

N, M = map(int, input().split())
floor = [list(input().strip()) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

count = 0

for i in range(N):
    for j in range(M):
        if not visited[i][j]:
            dfs(i, j)
            count += 1

print(count)
