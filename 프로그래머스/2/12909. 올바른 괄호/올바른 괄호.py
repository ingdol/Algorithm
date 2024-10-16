def solution(s):
    
    if len(s) % 2 != 0:
        return False
    
    stack = []
    
    for str in s:
        if str == '(':
            stack.append(str)
        if str == ')' and len(stack) > 0:
            stack.pop()
            
    if len(stack) == 0:
        return True
    else: return False