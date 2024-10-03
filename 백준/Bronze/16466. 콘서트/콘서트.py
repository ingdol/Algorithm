import sys
input = sys.stdin.readline

def find_smallest_ticket(N, sold_tickets):
    # 팔린 티켓 번호 정렬
    sold_tickets.sort()
    
    # 1부터 시작해서 가장 작은 팔리지 않은 번호 찾기
    smallest_ticket = 1
    for ticket in sold_tickets:
        if ticket == smallest_ticket:
            smallest_ticket += 1
        else:
            break
    
    return smallest_ticket

N = int(input())  # 팔린 티켓 수
sold_tickets = list(map(int, input().split()))  # 팔린 티켓 번호들

# 결과 출력
print(find_smallest_ticket(N, sold_tickets))
