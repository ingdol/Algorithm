import sys
input = sys.stdin.readline
from collections import deque

move_coordinate = [[-1, 2], [1, 2], [-2, 1], [2, 1], [-2, -1], [2, -1], [-1, -2], [1, -2]]

def bfs(start, end, l):
    if start == end:
        return 0
    queue = deque([[start[0], start[1], 0]])
    visitied[start[0]][start[1]] = 1
    
    while queue:
        stand_node = queue.popleft()
        x, y, cnt = stand_node
        for move in move_coordinate:
            move_x = x + move[0]
            move_y = y + move[1]
            
            if end[0] == move_x and end[1] == move_y:
                return cnt + 1
            if 0 <= move_x < l and 0 <= move_y < l and visitied[move_x][move_y] == 0:
                visitied[move_x][move_y] = 1
                queue.append([move_x, move_y, cnt + 1])
        

T = int(input())
for _ in range(T):
    l = int(input())
    visitied = [[0 for _ in range(l)] for _ in range(l)]
    start = list(map(int, input().split()))
    end = list(map(int, input().split()))
    print(bfs(start, end, l))