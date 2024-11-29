import sys
input = sys.stdin.readline

N = int(input())
arr = [int(input()) for _ in range(N)]
arr.sort(reverse=True)

result = []
for i in range(len(arr)):
    result.append(arr[i] * (i + 1))

print(max(result))