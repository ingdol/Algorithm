def dfs(x, y):
    if x >= N or y >= N:  # 맵을 벗어나는 경우
        return False
    if graph[x][y] == -1:  # 도착 지점에 도달한 경우
        return True
    if visited[x][y]:  # 이미 방문한 경우
        return False
    
    visited[x][y] = True  # 현재 위치 방문 처리
    jump = graph[x][y]  # 현재 위치에서 점프할 수 있는 칸 수
    
    # 오른쪽으로 이동
    if dfs(x, y + jump):
        return True
    # 아래쪽으로 이동
    if dfs(x + jump, y):
        return True
    
    return False

# 입력 받기
N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]

# DFS를 통해 끝점까지 도달할 수 있는지 확인
if dfs(0, 0):
    print("HaruHaru")
else:
    print("Hing")
