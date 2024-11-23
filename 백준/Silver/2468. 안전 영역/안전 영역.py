import sys
input = sys.stdin.readline

N = int(input())
set_list = set()
graph = []
for _ in range(N):
    num_list = list(map(int, input().split()))
    graph.append(num_list)
    for num in num_list:
        set_list.add(num)

directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

def bfs(inputY, inputX, h, visited):
    visited[inputY][inputX] = True
    queue = [[inputY, inputX]]

    while queue:
        cur_y, cur_x = queue.pop(0)
        for x, y in directions:
            now_x = cur_x + x
            now_y = cur_y + y
            if 0 <= now_x < N and 0 <= now_y < N and not visited[now_y][now_x] and graph[now_y][now_x] > h:
                queue.append([now_y, now_x])
                visited[now_y][now_x] = True
    return True

result = set()
for h in range(max(list(set_list)) + 1):
    cnt = 0
    visited = [[False for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if graph[i][j] > h and not visited[i][j]:
                if bfs(i, j, h, visited):
                    cnt += 1
    result.add(cnt)
print(max(list(result)))