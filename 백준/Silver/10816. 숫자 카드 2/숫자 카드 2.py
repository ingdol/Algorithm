from collections import defaultdict
import sys
input = sys.stdin.readline

N = int(input())
dic = defaultdict(int)
for num in input().strip().split():
    dic[num] += 1
    
M = int(input())
result = []
for num in input().strip().split():
    result.append(str(dic[num]))
print(' '.join(result))