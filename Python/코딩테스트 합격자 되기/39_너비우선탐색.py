# 코딩테스트 합격자 되기 - 문제 39
# https://github.com/dremdeveloper/codingtest_python/blob/main/solution/39.py
# https://github.com/kciter/coding-interview-js/blob/main/solution/39.js

from collections import defaultdict

def solution(arr, start):
    adj_list = defaultdict(list)
    for u, v in arr:
        adj_list[u].append(v)

    def bfs(start, result):
        queue = [start]
        visited = set()
        visited.add(start)
        result.append(start)

        while queue:
            cur = queue.pop(0)
            for neighbor in adj_list.get(cur, []):
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)
                    result.append(neighbor)
    result = []
    bfs(start, result)
    return result
print(solution([(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (3, 7), (4, 8), (5, 8), (6, 9), (7, 9)],1)) # 반환값 :[1, 2, 3, 4, 5, 6, 7, 8, 9]
print(solution([(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 0)],1)) # 반환값 : [1, 2, 3, 4, 5, 0]
