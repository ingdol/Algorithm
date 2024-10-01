import sys
input = sys.stdin.readline

n = int(input())  # 좌표의 개수 입력
stack = []
min_buildings = 0  # 최소 건물 개수를 저장할 변수

for _ in range(n):
    x, y = map(int, input().split())

    # 현재 높이가 스택의 높이보다 낮아지면, 스택에서 이전 높이를 pop
    while stack and stack[-1] > y:
        stack.pop()
    
    # 스택에 없거나, 현재 높이가 스택의 높이보다 크면 새로운 건물 시작
    if not stack or stack[-1] < y:
        stack.append(y)
        if y > 0:  # y가 0보다 크면 새로운 건물로 간주
            min_buildings += 1

# 최종적으로 계산된 건물 개수 출력
print(min_buildings)
