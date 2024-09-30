import sys
input = sys.stdin.readline

def dfs(x, y):
    if x <= -1 or x >= r or y <= -1 or y >= c:
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False

r, c = map(int, input().split())

graph = []
for i in range(r):
    column = input().strip()
    column_list = []
    for item in column:
        if item == '.':
            column_list.append(1)
        else: column_list.append(0)
    graph.append(column_list)

count = 0
for i in range(r):
    for j in range(c):
        if dfs(i, j) == True:
            count += 1
            
print(count)
