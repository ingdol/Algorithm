import sys
input = sys.stdin.readline
from collections import deque

directions = [-1, 1, 2]
def bfs(x, k):
    queue = deque([x])
    visited = [-1] * 100001
    visited[x] = 0

    while queue:
        current = queue.popleft()

        if current == k:
            return visited[current]
        
        for next_pos in (current - 1, current + 1, current * 2):
            if 0 <= next_pos <= 100000 and visited[next_pos] == -1:
                visited[next_pos] = visited[current] + 1
                queue.append(next_pos)
            

N, K = map(int, input().split())
print(bfs(N, K))