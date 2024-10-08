import sys
input = sys.stdin.readline
from collections import deque

directions = [(-1, 2), (1, 2), (-2, 1), (2, 1), (-2, -1), (2, -1), (-1, -2), (1, -2)]

def bfs(start, end, l):
    visited = [[False for _ in range(l)] for _ in range(l)]
    queue = deque([[start[0], start[1], 0]])
    visited[start[0]][start[1]] = True

    while queue:
        cur_x, cur_y, cur_cnt = queue.popleft()

        if [cur_x, cur_y] == end:
            return cur_cnt

        for direction in directions:
            move_x = cur_x + direction[0]
            move_y = cur_y + direction[1]
            
            if 0 <= move_x < l and 0 <= move_y < l and not visited[move_x][move_y]:
                visited[move_x][move_y] = True
                queue.append([move_x, move_y, cur_cnt + 1])
        
T = int(input())
for _ in range(T):
    l = int(input())
    start = list(map(int, input().split()))
    end = list(map(int, input().split()))
    print(bfs(start, end, l))