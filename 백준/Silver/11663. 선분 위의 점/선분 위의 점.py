import sys
input = sys.stdin.readline

def lower_bound(arr, target):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] >= target:
            right = mid
        else:
            left = mid + 1
    return left

def upper_bound(arr, target):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] > target:
            right = mid
        else:
            left = mid + 1
    return left

N, M = map(int, input().split())
points = list(map(int, input().split()))
points.sort()

for _ in range(M):
    start, end = map(int, input().split())
    start_idx = lower_bound(points, start)
    end_idx = upper_bound(points, end)
    print(end_idx - start_idx)
