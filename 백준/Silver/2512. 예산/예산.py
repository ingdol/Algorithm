import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
s = int(input())

left, right = 0, max(arr)

while left <= right:
    mid = (left + right) // 2
    total = sum(min(mid, x) for x in arr)
    
    if total <= s:
        left = mid + 1
    else:
        right = mid - 1

print(right)
