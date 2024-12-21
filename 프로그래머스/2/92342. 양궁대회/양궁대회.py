from itertools import combinations_with_replacement

def solution(n, info):
    max_diff = -1
    best_shot = [-1]
    
    for shots in combinations_with_replacement(range(11), n):
        ryan = [0] * 11
        for s in shots:
            ryan[10 - s] += 1

        ryan_score = 0
        apeach_score = 0

        for i in range(11):
            if ryan[i] > info[i]:
                ryan_score += 10 - i
            elif info[i] > 0:
                apeach_score += 10 - i

        if ryan_score > apeach_score:
            diff = ryan_score - apeach_score
            if diff > max_diff:
                max_diff = diff
                best_shot = ryan

    return best_shot
