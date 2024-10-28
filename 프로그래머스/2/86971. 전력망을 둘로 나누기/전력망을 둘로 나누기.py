def bfs(n, graph, start):
    visited = [0 for _ in range(n + 1)]
    queue = [start]
    visited[start] = 1
    cnt = 1
    while queue:
        cur = queue.pop(0)
        for neighbor in graph[cur]:
            if visited[neighbor] == 0:
                queue.append(neighbor)
                visited[neighbor] = 1
                cnt += 1
    return cnt
    
def solution(n, wires):
    answer = []
    graph = [[] for _ in range(n + 1)]
    for wire in wires:
        graph[wire[0]].append(wire[1])
        graph[wire[1]].append(wire[0])
    
    for wire in wires:
        graph[wire[0]].remove(wire[1])
        graph[wire[1]].remove(wire[0])
        
        cnt1 = bfs(n, graph, wire[0])
        cnt2 = n - cnt1
        
        answer.append(abs(cnt1 - cnt2))
        
        graph[wire[0]].append(wire[1])
        graph[wire[1]].append(wire[0])
        
    return min(answer)