import sys
input = sys.stdin.readline
sys.setrecursionlimit(100001)

def dfs(current_node):
    # 현재 노드가 이미 방문했거나 팬클럽이 있는 노드인 경우 종료
    if visited[current_node] or current_node in fanclub_nodes:
        return
    visited[current_node] = True

    # 더 이상 이동할 간선이 없는 경우 팬클럽을 만나지 않으면 "yes" 출력
    if not graph[current_node]:
        print("yes")
        exit(0)

    # 다음 노드로 이동
    for next_node in graph[current_node]:
        if next_node not in fanclub_nodes and not visited[next_node]:
            dfs(next_node)

if __name__ == "__main__":
    # 정점과 간선의 개수 입력
    N, M = map(int, input().split())

    # 그래프 초기화
    graph = [[] for _ in range(N + 1)]
    visited = [False] * (N + 1)

    # 간선 정보 입력
    for _ in range(M):
        from_node, to_node = map(int, input().split())
        graph[from_node].append(to_node)

    # 팬클럽이 있는 정점 정보 입력
    S = int(input())
    fanclub_nodes = set(map(int, input().split()))

    # 1번 노드에서 DFS 시작
    dfs(1)

    # 모든 경로를 탐색해도 종료되지 않으면 팬클럽을 만나므로 "Yes" 출력
    print("Yes")
