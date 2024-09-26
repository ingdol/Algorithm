import sys
input = sys.stdin.readline

N = int(input())

for i in range(N):
    words = input().strip().split()
    words.reverse()
    print(f"Case #{i + 1}: {' '.join(words)}")