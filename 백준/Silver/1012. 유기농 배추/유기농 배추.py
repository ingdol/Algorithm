import sys
input = sys.stdin.readline
from collections import deque

directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
def bfs(x, y):
    queue = deque([(x, y)])
    visited[x][y] = 1

    while queue:
        cur_x, cur_y = queue.popleft()

        for direction in directions:
            new_x = cur_x + direction[0]
            new_y = cur_y + direction[1]
            
            if 0 <= new_x < N and 0 <= new_y < M and visited[new_x][new_y] == 0 and graph[new_x][new_y] == 1:
                visited[new_x][new_y] = 1
                queue.append((new_x, new_y))

    


T = int(input())

for _ in range(T):
    M, N, K = map(int, input().split())
    graph = [[0 for _ in range(M)] for _ in range(N)]
    visited = [[0 for _ in range(M)] for _ in range(N)]
    for i in range(K):
        y, x = map(int, input().strip().split(' '))
        graph[x][y] = 1
    
    worm_count = 0

    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1 and visited[i][j] == 0:
                bfs(i, j)
                worm_count += 1
    print(worm_count)