import sys
input = sys.stdin.readline

test_case_num = int(input())
university_list = []
for _ in range(test_case_num):
    university_num = int(input())
    for _ in range(university_num):
        name, amount = input().strip().split()
        university_list.append((int(amount), name))
    desc_university_list = sorted(university_list, reverse=True)
    print(desc_university_list[0][1])

