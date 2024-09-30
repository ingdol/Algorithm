T = int(input())  # 테스트 케이스 수 입력

for _ in range(T):
    N, M = map(int, input().split())  # 국가 수 N과 비행기 종류 M 입력
    for _ in range(M):
        a, b = map(int, input().split())  # 비행기 스케줄 (a, b) 입력
    print(N - 1)  # 최소 간선 수는 항상 N - 1
