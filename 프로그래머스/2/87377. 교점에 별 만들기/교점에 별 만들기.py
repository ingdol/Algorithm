from itertools import combinations
def solution(line):
    combi_list = list(combinations(line, 2))
    arr = []
    print_line = []
    x_list = []
    y_list = []
    for a, b in combi_list:
        A = a[0]
        B = a[1]
        E = a[2]
        C = b[0]
        D = b[1]
        F = b[2]
        if A*D - B*C != 0:
            x = (B*F - E*D) // (A*D - B*C)
            x_X = (B*F - E*D) / (A*D - B*C)
            y = (E*C - A*F) // (A*D - B*C)
            y_Y = (E*C - A*F) / (A*D - B*C)
            if x == x_X and y == y_Y:
                print_line.append([x, y])
                x_list.append(x)
                y_list.append(y)
    answer = []
    for j in range(min(y_list), max(y_list) + 1):
        line = ''
        for i in range(min(x_list), max(x_list) + 1):
            flag = 0
            for x, y in print_line:
                if x == i and y == j and flag != 1:
                    line += '*'
                    flag = 1
            if flag == 0:
                line += '.'
        answer.append(line)
    answer.reverse()
    return answer