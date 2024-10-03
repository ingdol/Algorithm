# 입력 받기
P1, Y1, S1 = input().split()
P2, Y2, S2 = input().split()
P3, Y3, S3 = input().split()

# 정수형으로 변환
P1, Y1 = int(P1), int(Y1)
P2, Y2 = int(P2), int(Y2)
P3, Y3 = int(P3), int(Y3)

# 첫 번째 방법: 입학 연도를 100으로 나눈 나머지를 오름차순으로 정렬한 후 이어 붙이기
years_mod = sorted([Y1 % 100, Y2 % 100, Y3 % 100])
team_name_1 = ''.join(map(str, years_mod))

# 두 번째 방법: 해결한 문제 수를 기준으로 내림차순 정렬한 후 성씨의 첫 글자를 붙이기
participants = [(P1, S1), (P2, S2), (P3, S3)]
participants_sorted = sorted(participants, key=lambda x: -x[0])  # 문제 수 기준 내림차순
team_name_2 = ''.join([p[1][0] for p in participants_sorted])

# 결과 출력
print(team_name_1)
print(team_name_2)
