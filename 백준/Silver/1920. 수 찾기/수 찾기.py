import sys
input = sys.stdin.readline

def binary_search(number_list, target):
    left, right = 0, len(number_list) - 1
    while left <= right:
        mid = (left + right) // 2

        if number_list[mid] == target:
            return 1
        elif number_list[mid] >= target:
            right = mid - 1
        else:
            left = mid + 1
    return 0

list_num = int(input())
number_list = list(map(int, input().split()))
number_list.sort()

target_list_num = int(input())
target_list = list(map(int, input().split()))

for target in target_list:
   print(binary_search(number_list, target))
   