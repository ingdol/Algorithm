def bfs(visited, graph, start, visite_node):
    visited[start] = 1
    stack = [[start, 1]]
    while stack:
        cur, cnt = stack.pop(0)
        for node in graph[cur]:
            if visited[node] == 0:
                visited[node] = 1
                stack.append([node, cnt + 1])
                visite_node.append([cnt + 1, node])
    
def solution(n, edge):
    answer = 0
    graph = [[] for _ in range(n + 1)]
    visited = [0 for _ in range(n + 1)]
    for i, j in edge:
        graph[i].append(j)
        graph[j].append(i)
    for i in range(len(graph)):
        graph[i] = sorted(graph[i])
        
    visite_node = []
    bfs(visited, graph, 1, visite_node)
    visite_node.sort(reverse=True)
    
    max_visited = visite_node[0][0]
    for i, j in visite_node:
        if i == max_visited:
            answer += 1
        
    return answer