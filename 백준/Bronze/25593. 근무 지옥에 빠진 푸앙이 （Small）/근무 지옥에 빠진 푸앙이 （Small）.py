from collections import defaultdict
import sys
input = sys.stdin.readline

N = int(input())
shifts = [4, 6, 4, 10]

dic = defaultdict(int)

for _ in range(N):
    for shift in range(4):
        names = input().split()
        for name in names:
            if name == '-': 
                continue
            else: dic[name] += shifts[shift]

if dic:
    if max(dic.values()) - min(dic.values()) <= 12:
        print("Yes")
    else:
        print("No")
else:
    print("Yes")
