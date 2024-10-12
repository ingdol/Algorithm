def solution(numbers):
    numbers = list(map(str, numbers))
    numbers = sorted(numbers, key=lambda item:item*3, reverse = True)
    
    return str(int(''.join(numbers)))