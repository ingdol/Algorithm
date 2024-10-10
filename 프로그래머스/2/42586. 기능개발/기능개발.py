import math

def solution(progresses, speeds):
    answer = []
    queue = []
    for i in range(len(progresses)):
        queue.append(math.ceil((100 - progresses[i]) / speeds[i]))
    
    cnt = 0
    prev = queue[0]
    for i in range(1, len(queue)):
        if prev < queue[i]:
            answer.append(cnt + 1)
            prev = queue[i]
            cnt = 0
        else:
            cnt += 1
    answer.append(cnt + 1)
    
    return answer