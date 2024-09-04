N = int(input())
for j in range(1, N + 1):
    print("*" * (j) + " " * (N - j) * 2 + "*" * (j))
for j in range(N - 1, 0, -1):
    print("*" * (j) + " " * (N - j) * 2 + "*" * (j))