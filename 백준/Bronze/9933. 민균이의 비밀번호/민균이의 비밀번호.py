import sys
input = sys.stdin.readline

N = int(input())
key_list = []
for _ in range(N):
    key_list.append(input().strip())

for key in key_list:
    reverse_key = key[::-1]
    if reverse_key in key_list:
        key_length = len(reverse_key)
        print(key_length, reverse_key[key_length//2])
        break