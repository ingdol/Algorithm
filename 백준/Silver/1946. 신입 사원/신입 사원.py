import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    rank_list = []
    for _ in range(N):
        rank_list.append(list(map(int, input().split())))
    rank_list.sort()
    pass_num = 1
    compare_rank = rank_list[0][1]

    for i in range(1, len(rank_list)):
        if compare_rank > rank_list[i][1]:
            pass_num += 1
            compare_rank = rank_list[i][1]
    print(pass_num)