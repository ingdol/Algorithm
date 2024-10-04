import sys
input = sys.stdin.readline

Y_list = []
P_S_list = []

for _ in range(3):
    P, Y, S = input().strip().split()
    Y_list.append(int(Y))
    P_S_list.append((int(P), S))

result_1 = sorted(Y_list)
result_1 = list(map(lambda y : y % 100, result_1))
result_1 = ''.join(map(str, result_1))
print(result_1)

result_2 = sorted(P_S_list, reverse=True)
result_2 = list(map(lambda list : list[1][0], result_2))
result_2 = ''.join(result_2)
print(result_2)