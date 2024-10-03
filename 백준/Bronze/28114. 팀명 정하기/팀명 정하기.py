import sys
input = sys.stdin.readline

# 입력 받기
data = [input().split() for _ in range(3)]
participants = [(int(P), int(Y), S) for P, Y, S in data]

# 첫 번째 방법: 입학 연도를 100으로 나눈 나머지를 오름차순으로 정렬한 후 이어 붙이기
team_name_1 = ''.join(map(str, sorted([Y % 100 for _, Y, _ in participants])))

# 두 번째 방법: 해결한 문제 수를 기준으로 내림차순 정렬한 후 성씨의 첫 글자를 붙이기
team_name_2 = ''.join([S[0] for _, _, S in sorted(participants, key=lambda x: -x[0])])

# 결과 출력
print(team_name_1)
print(team_name_2)