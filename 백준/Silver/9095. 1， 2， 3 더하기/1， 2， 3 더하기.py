import sys
input = sys.stdin.readline

N = int(input())
arr = [int(input()) for _ in range(N)]

big_num = max(arr)
dp = [0] * (big_num+1)
dp[1] = 1
dp[2] = 2
dp[3] = 4
for i in range(4, big_num+1):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

for i in arr:
    print(dp[i])