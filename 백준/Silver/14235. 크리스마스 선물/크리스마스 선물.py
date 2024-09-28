from heapq import heappop, heappush
import sys
input = sys.stdin.readline

n = int(input())

heap = []

for _ in range(n):
    spot = input().strip()

    if spot == '0':
        if heap:
            print(-heappop(heap))
        else:
            print(-1)
    else:
        gift_list = list(map(int, spot.split(' ')))
        
        for gift_index in range(1, gift_list[0] + 1):
            gift = gift_list[gift_index]
            heappush(heap, -(gift))