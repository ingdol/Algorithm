from itertools import permutations

def checkPrime(n):
    if n < 2:
        return False
    
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def solution(numbers):
    answer = set()
    
    for i in range(1, len(numbers) + 1):
        perms = permutations(numbers, i)
        for perm in perms:
            num_str = ''.join(perm)
            if checkPrime(int(num_str)):
                answer.add(int(num_str)) 
        
    return len(set(answer))