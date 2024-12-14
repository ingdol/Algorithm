import sys
input = sys.stdin.readline

N = int(input())
str1 = input().strip()
str2 = input().strip()


def check(str1, str2):
    vowels = ['a', 'e', 'i', 'o', 'u']
    if str1[0] != str2[0] or str1[-1] != str2[-1]:
        return False

    test_str1 = sorted(str1[1:-1])
    test_str2 = sorted(str2[1:-1])
    if test_str1 != test_str2:
        return False
    
    str1_fin = ''
    str2_fin = ''
    for i in range(1, N - 1):
        if str1[i] not in vowels:
            str1_fin = str1_fin + str1[i]
        if str2[i] not in vowels:
            str2_fin = str2_fin + str2[i]
    
    if str1_fin == str2_fin:
        return True
    else: return False

if check(str1, str2):
    print('YES')
else: print('NO')