import math;

def isPrimeNum(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False

    return True
    
def solution(n, k):
    answer = 0
    print(n, k)
    num = []
    while n > 0:
        num.append(n % k)
        n //= k
    num = list(reversed(num))
    print(num)
    prime_check = []
    str_list = []
    inner_str = []
    for n in num:
        if n != 0:
            inner_str.append(str(n))
        print(inner_str)
        if n == 0:
            str_list.append(inner_str)
            inner_str = []
    str_list.append(inner_str)
    print(str_list)
    
    for num_str in str_list:
        print(''.join(num_str))
        num_str = ''.join(num_str)
        if num_str != '' and num_str != '1':
            if(isPrimeNum(int(num_str))):
                answer += 1
    
    return answer