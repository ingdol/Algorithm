# 코딩테스트 합격자 되기 - 문제 38
# https://github.com/kciter/coding-interview-js/blob/main/solution/38.js
# 재귀함수
def solution(arr, start):

    adj_list = defaultdict(list)
    for u, v in reversed(arr):
        adj_list[u].append(v)

    def dfs(node, visited, result):
        visited.add(node)
        result.append(node)
        for neighbor in adj_list.get(node, []):
            print(neighbor)
            if neighbor not in visited:
                dfs(neighbor, visited, result)

    visited = set()
    result = []
    dfs(start, visited, result)
    return result

# stack
def solution2(arr, start):
    visited = defaultdict(int)
    graph = defaultdict(list)

    for u, v in reversed(arr):
        visited[u] = 0
        graph[u].append(v)
    stack = [start]

    res = []
    while stack:
        cur_node = stack.pop()
        if visited[cur_node] == 0:
            for node in graph[cur_node]:
                stack.append(node)
            visited[cur_node] = 1
            res.append(cur_node)
    return res

print(solution([['A', 'B'], ['B', 'C'], ['C', 'D'], ['D', 'E']], 'A')) # 반환값 : ['A', 'B', 'C', 'D', 'E']
print(solution([['A', 'B'], ['A', 'C'], ['B', 'D'], ['B', 'E'], ['C', 'F'], ['E', 'F']], 'A')) # 반환값 : ['A', 'B', 'D', 'E', 'F', 'C']
