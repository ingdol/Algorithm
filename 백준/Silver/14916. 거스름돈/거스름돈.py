import sys
input = sys.stdin.readline

price = int(input())
coins = [5, 2]
cnt = 0
rest = price % 5

for coin in coins:
    if price >= coin:
        if coin == 5 and rest % 2 != 0:
            cnt = price // coin - 1
            price -= cnt * coin
        else:
            cnt += price // coin
            price %= coin

if price == 0:
    print(cnt)
else: print(-1)