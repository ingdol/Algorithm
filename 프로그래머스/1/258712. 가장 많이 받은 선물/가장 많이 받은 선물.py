from itertools import combinations

def solution(friends, gifts):
    gift_list = [[0 for _ in range(len(friends))] for _ in range(len(friends))]
    gift_num = [0 for _ in range(len(friends))]
    gift_given = [0 for _ in range(len(friends))]
    for gift in gifts:
        A, B = gift.split() 
        gift_list[friends.index(A)][friends.index(B)] += 1
        gift_num[friends.index(A)] += 1
        gift_num[friends.index(B)] -= 1
    combi_list = list(combinations(friends, 2))
    for A, B in combi_list:
        AtoB = gift_list[friends.index(A)][friends.index(B)]
        BtoA = gift_list[friends.index(B)][friends.index(A)]
        if AtoB > BtoA:
            gift_given[friends.index(A)] += 1
        elif AtoB < BtoA:
            gift_given[friends.index(B)] += 1
        else: 
            if gift_num[friends.index(A)] > gift_num[friends.index(B)]:
                gift_given[friends.index(A)] += 1
            elif gift_num[friends.index(A)] < gift_num[friends.index(B)]:
                gift_given[friends.index(B)] += 1
    return max(gift_given)