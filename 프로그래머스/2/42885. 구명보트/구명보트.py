def solution(people, limit):
    answer = 0
    end = len(people) - 1
    people.sort()
    start = 0
    target = people[start]
    while end > start:
        sum = target + people[end]
        if sum <= limit:
            end -= 1
            start += 1
            target = people[start]
        else: 
            end -= 1
        answer += 1
        if end == start: answer += 1
    return answer