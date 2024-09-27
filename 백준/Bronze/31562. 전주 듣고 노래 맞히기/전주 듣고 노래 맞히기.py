import sys
input = sys.stdin.readline

N, M = list(map(int, input().split()))

dic = {}
for _ in range(N):
    line = input().split()
    a_list = ' '.join(line[2:5])
    if a_list in dic:
        dic[a_list] = '?'
    else: dic[a_list] = line[1]

for _ in range(M):
    b_list = input().strip()
    if b_list in dic:
        print(dic[b_list])
    else: print('!')