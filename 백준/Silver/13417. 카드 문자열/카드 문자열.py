import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
for _ in range(N):
    n = int(input())
    str_list = list(input().split())
    card_sort = deque()
    card_sort.append(str_list[0])
    for i in range(1, n):
        if ord(str_list[i]) <= ord(card_sort[0]):
            card_sort.appendleft(str_list[i])
        else: card_sort.append(str_list[i])
    print(''.join(card_sort))