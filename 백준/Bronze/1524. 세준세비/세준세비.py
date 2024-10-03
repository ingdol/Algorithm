import sys
input = sys.stdin.readline

# 테스트 케이스의 개수 입력
test_case_num = int(input())

for _ in range(test_case_num):
    input()  # 빈 줄 무시
    N, M = map(int, input().strip().split())  # 세준이(N)와 세비(M)의 병사 수 입력

    # 세준이의 병사들 (내림차순 정렬)
    sejun_soldier = sorted(map(int, input().strip().split()), reverse=True)
    # 세비의 병사들 (내림차순 정렬)
    sebi_soldier = sorted(map(int, input().strip().split()), reverse=True)

    # 두 병사 리스트의 인덱스 초기화
    sejun_index = sebi_index = 0

    # 전투 시작
    while sejun_index < N and sebi_index < M:
        # 세준이 병사가 더 약하면 세준이 병사 제거
        if sejun_soldier[sejun_index] < sebi_soldier[sebi_index]:
            sejun_index += 1
        # 세비 병사가 더 약하면 세비 병사 제거
        elif sejun_soldier[sejun_index] > sebi_soldier[sebi_index]:
            sebi_index += 1
        # 동일한 힘을 가진 병사들이 있으면 세비 병사 제거
        else:
            sebi_index += 1
    
    # 결과 출력: 세준이 병사가 남았으면 'S', 세비 병사가 남았으면 'B', 둘 다 남으면 'C'
    if sejun_index == N and sebi_index == M:
        print("C")
    elif sejun_index == N:
        print("B")
    else:
        print("S")
