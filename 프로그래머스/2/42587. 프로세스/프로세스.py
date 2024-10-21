from collections import deque
def solution(priorities, location):
    answer = 0
    queue = deque()
    for i in range(len(priorities)):
        queue.append((priorities[i], i))
    max_num = max(queue)
    list = []
    while len(queue) > 1:
        target_num = queue.popleft()
        
        if target_num[0] < max_num[0]:
            queue.append(target_num)
        else:
            list.append(target_num)
            max_num = max(queue)
    list.append(queue[0])
    
    for i in range(len(list)):
        if location == list[i][1]:
            return i + 1
        
    # return list