import sys
input = sys.stdin.readline

price = int(input())
coin = [5, 2]
i = 0
cnt = 0
none_price = [1, 3]
if price in none_price : cnt = -1
else:
    while price > 0:
        cnt += price // coin[i]
        price %= coin[i]
        if price % 2 != 0:
            cnt -= 1
            price += coin[i]
        i += 1

print(cnt)