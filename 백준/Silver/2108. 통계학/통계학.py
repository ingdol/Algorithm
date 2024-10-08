import sys
input = sys.stdin.readline
from collections import defaultdict

N = int(input())

if N == 1:
    n = int(input())
    print(n)
    print(n)
    print(n)
    print(0)
else: 
    N_list = []
    for _ in range(N):
        N_list.append(int(input()))
    N_list.sort()
    print(round(sum(N_list) / N))
    print(N_list[N//2])

    dic = defaultdict(int)
    for n in N_list:
        dic[n] += 1
    sorted_dic = sorted(dic.items(), key=lambda item : item[1], reverse=True)
    if sorted_dic[0][1] == sorted_dic[1][1]:
        print(sorted_dic[1][0])
    else: print(sorted_dic[0][0])

    print(max(N_list) - min(N_list))