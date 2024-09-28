from collections import defaultdict
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input()) 
    clothes = defaultdict(int)
    
    for _ in range(n):
        name, category = input().strip().split()
        clothes[category] += 1
    
    result = 1
    for count in clothes.values():
        result *= (count + 1)
    
    print(result - 1)  