import sys
input = sys.stdin.readline

# 방향 배열 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, num):
    # 길이가 6이 되면 집합에 추가하고 종료
    if len(num) == 6:
        numbers.add(num)
        return
    
    # 상하좌우로 이동
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        # 범위를 벗어나지 않는지 체크
        if 0 <= nx < 5 and 0 <= ny < 5:
            dfs(nx, ny, num + grid[nx][ny])

# 입력 받기
grid = [input().split() for _ in range(5)]

# 서로 다른 6자리 숫자를 저장할 집합
numbers = set()

# 각 위치에서 DFS 탐색 시작
for i in range(5):
    for j in range(5):
        dfs(i, j, grid[i][j])

# 집합에 저장된 숫자의 개수를 출력
print(len(numbers))
