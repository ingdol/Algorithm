from heapq import heappush, heappop, nlargest
import sys
input = sys.stdin.readline

N = int(input())
dasom_vote = int(input())
heap = []

for _ in range(N - 1):
    heappush(heap, -int(input()))

vote_num = 0

while N > 1 and dasom_vote <= -heap[0]:
    max_vote = -heappop(heap)
    dasom_vote += 1
    vote_num += 1
    heappush(heap, -(max_vote - 1))
    
print(vote_num)

