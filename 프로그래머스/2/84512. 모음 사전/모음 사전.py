def dfs(arr, current_string):
    if len(current_string) <= 5:
        result.append(current_string)
        
    if len(current_string) == 5:
        return
    
    for s in arr:
        dfs(arr, current_string + s)
            
def solution(word):
    arr = ['A', 'E', 'I', 'O', 'U']
    
    global result
    result = []
    
    current_string = ''
    dfs(arr, current_string)
    
    result.sort()
    
    return result.index(word)