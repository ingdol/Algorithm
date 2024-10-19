def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    for i in citations:
        if answer < i:
            answer += 1
    return answer