import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(node):
    visited[node] = 1
    
    for inner_node in graph[node]:
        if visited[inner_node] == 0:
            cnt[0] += 1
            dfs(inner_node)

computer_cnt = int(input())
computer_line = int(input())

graph = [[] for _ in range(computer_cnt + 1)]
for _ in range(computer_line):
    com_1, com_2 = map(int, input().split())
    graph[com_1].append(com_2)
    graph[com_2].append(com_1)

visited = [0 for _ in range(computer_cnt + 1)]
cnt = [0]
dfs(1)
print(cnt[0])
