import heapq
import sys

input = sys.stdin.readline

def min_merge_cost(chapters):
    heapq.heapify(chapters)  # 리스트를 힙 구조로 변환
    total_cost = 0
    
    # 파일이 하나로 합쳐질 때까지 반복
    while len(chapters) > 1:
        # 가장 작은 두 파일을 꺼내서 합침
        first = heapq.heappop(chapters)
        second = heapq.heappop(chapters)
        merge_cost = first + second
        total_cost += merge_cost
        # 합친 결과를 다시 힙에 넣음
        heapq.heappush(chapters, merge_cost)
    
    return total_cost

# 테스트 케이스 입력
test_case_num = int(input())

for _ in range(test_case_num):
    chapter_num = int(input())
    chapters = list(map(int, input().split()))
    # 최소 비용 계산
    print(min_merge_cost(chapters))
