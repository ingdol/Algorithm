from heapq import heappush, heappop, nlargest
import sys
input = sys.stdin.readline

N = int(input())
heap = []
dasom_vote = int(input())
vote_num = 0
for _ in range(N - 1):
    heappush(heap, int(input()))
heap = nlargest(len(heap), heap)

while N > 1 and dasom_vote <= heap[0]:
    dasom_vote += 1
    vote_num += 1
    heappush(heap, heappop(heap) - 1)
    heap = nlargest(len(heap), heap)
    
print(vote_num)