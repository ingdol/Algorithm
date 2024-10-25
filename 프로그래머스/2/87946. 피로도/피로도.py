from itertools import permutations

def solution(k, dungeons):
    max_dungeons = 0
    
    for perm in permutations(dungeons):
        health = k
        cnt = 0
        for dungeon in perm:
            if health >= dungeon[0]:
                health -= dungeon[1]
                cnt += 1
            else:
                break
        max_dungeons = max(max_dungeons, cnt)
    
    return max_dungeons
