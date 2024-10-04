import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    input()
    N, M = list(map(int, input().split()))
    N_list = list(map(int, input().split()))
    M_list = list(map(int, input().split()))

    while N_list and M_list:
        if N_list[-1] >= M_list[-1]:
            M_list.pop()
        else:
            N_list.pop()
    
    if len(N_list) > len(M_list) :
        print('S')
    else: print('B')

