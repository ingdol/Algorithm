from heapq import heappop, heappush
import sys
input = sys.stdin.readline

N, H, T = list(map(int, input().split(' ')))

heap = []

for _ in range(N):
    height = int(input())
    heappush(heap, -height)

T_use_count = 0

while T > 0 and -heap[0] >= H and -heap[0] != 1:
    max_height = -heappop(heap)
    heappush(heap, -(max_height//2))
    T -= 1
    T_use_count += 1

if H > -heap[0]:
    print('YES')
    print(T_use_count)
else:
    print('NO')
    print(-heap[0])