import sys
input = sys.stdin.readline

T = int(input()) # 테스트 케이스의 개수

for _ in range(T):
    N = int(input()) # 지원자 수
    rank_list = [] # 등수 리스트

    for _ in range(N):
		    # 등수 리스트에 [서류심사 등수, 면접시험 등수] 입력
        rank_list.append(tuple(map(int, input().split()))) 
    
    rank_list.sort() # 서류심사 등수를 기준으로 오름차순 정렬

    pass_num = 1 # 최종 합격자 수
    # 서류심사 1등의 면접시험 등수를 기준으로 비교
    compare_rank = rank_list[0][1] 
    
    for i in range(1, N):
        # 해당 지원자가 서류심사 등수가 더 높은 지원자보다 면접시험 등수가 더 높다면 합격
        if compare_rank > rank_list[i][1]: 
            pass_num += 1
            compare_rank = rank_list[i][1]
            
    print(pass_num)