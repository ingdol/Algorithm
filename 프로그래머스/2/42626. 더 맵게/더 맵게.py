from heapq import heappush, heappop, heapify
def solution(scoville, K):
    answer = 0
    heapify(scoville)
    
    while scoville[0] < K:
        try:
            heappush(scoville, heappop(scoville) + heappop(scoville) * 2)
        except:
            return -1
        answer += 1
    
    return answer