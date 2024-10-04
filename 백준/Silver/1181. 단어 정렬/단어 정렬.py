import sys
input = sys.stdin.readline
from collections import defaultdict

N = int(input())

words = defaultdict(list)
for _ in range(N):
    word = input().strip()
    length = len(word)
    words[length].append(word)
len_shortest_list = sorted(words.items(), key = lambda item: item[0])

for word in len_shortest_list:
    dictionary_sorted_list = sorted(set(word[1]))
    for res_word in dictionary_sorted_list:
        print(res_word)
