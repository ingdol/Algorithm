import sys
input = sys.stdin.readline

def build_tree(buildings, level, levels):
    # 중간 값을 루트로 하여 트리를 재귀적으로 구성
    mid = len(buildings) // 2
    levels[level].append(buildings[mid])  # 해당 레벨에 현재 노드를 추가

    # 왼쪽 서브트리 처리
    if mid > 0:
        build_tree(buildings[:mid], level + 1, levels)
    
    # 오른쪽 서브트리 처리
    if mid + 1 < len(buildings):
        build_tree(buildings[mid + 1:], level + 1, levels)

# 입력 처리
K = int(input())  # 트리의 깊이
buildings = list(map(int, input().split()))  # 중위 순회로 방문한 빌딩 번호 리스트

# 각 레벨을 저장할 리스트 (K개 레벨)
levels = [[] for _ in range(K)]

# 트리 구성 및 레벨별 노드 저장
build_tree(buildings, 0, levels)

# 결과 출력
for level in levels:
    print(*level)