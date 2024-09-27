import sys
input = sys.stdin.readline

N = int(input())
dic = {}
for _ in range(N):
    dic[input().strip()] = 0
key_list = dic.keys()

for key in key_list:
    reverse_key = key[::-1]
    if reverse_key in dic:
        key_length = len(reverse_key)
        print(key_length, reverse_key[key_length//2])
        break