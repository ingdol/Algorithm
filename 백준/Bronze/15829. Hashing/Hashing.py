import sys
input = sys.stdin.readline

M = 1234567891

L = int(input())
str = input().strip()
sum = 0
for i in range(L):
    sum = (sum + (ord(str[i]) - 96) * pow(31, i, M)) % M
print(sum)