arr = input().split()
sum = 0
for x in arr:
    sum += int(x) ** 2
print(sum % 10)