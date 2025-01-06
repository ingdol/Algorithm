import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
graph = [list(map(int, input().strip())) for _ in range(n)]
visited = [[False for _ in range(n)] for _ in range(n)]
direction = [[1, 0], [-1, 0], [0, 1], [0, -1]]
answer = []
def bfs(y, x):
    count = 1
    visited[y][x] = True
    q = deque([[y, x]])

    while q:
        cur_y, cur_x = q.popleft()
        
        for dx, dy in direction:
            move_x, move_y = cur_x + dx, cur_y + dy
            if 0 <= move_x < n and 0 <= move_y < n and graph[move_y][move_x] == 1 and visited[move_y][move_x] == False:
                visited[move_y][move_x] = True
                q.append([move_y, move_x])
                count += 1
    answer.append(count)

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and not visited[i][j]:
            bfs(i, j)

print(len(answer))
answer.sort()
for num in answer:
    print(num)