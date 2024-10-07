import sys
input = sys.stdin.readline
from collections import deque

coordinates = [[-1, 0], [1, 0], [0, -1], [0, 1]]
def bfs(start, end):
    queue = deque([[start[0], start[1], 0]])
    visited[start[0]][start[1]] = 1
    cnt = 0
    result = []

    while queue:
        stand_node = queue.popleft()

        for coordinate in coordinates:
            move_x = stand_node[0] + coordinate[0]
            move_y = stand_node[1] + coordinate[1]
            cnt = stand_node[2]

            if move_x == end[0] and move_y == end[1]:
                result.append(cnt)
                return result
            
            if 0 <= move_x < 10 and 0 <= move_y < 10 and visited[move_x][move_y] == 0:
                visited[move_x][move_y] = 1
                queue.append([move_x, move_y, cnt + 1])

visited = [[0 for _ in range(10)] for _ in range(10)]
for i in range(10):
    line = input()
    for j in range(10):
        if line[j] == 'L':
            L = [i, j]
        elif line[j] == 'B':
            B = [i, j]
        elif line[j] == 'R':
            visited[i][j] = 1

cow_cnt = bfs(L, B)
print(max(set(cow_cnt)))