import sys

# 입력 받기
input = sys.stdin.readline
n = int(input())
coords = list(map(int, input().split()))

# 좌표를 정렬하고 중복 제거한 리스트 생성
sorted_coords = sorted(set(coords))

# 각 좌표에 대한 압축된 값을 저장할 딕셔너리 생성
coord_dict = {coord: idx for idx, coord in enumerate(sorted_coords)}

# 원래 좌표 리스트를 압축된 값으로 변환
compressed_coords = [coord_dict[coord] for coord in coords]

# 결과 출력
print(" ".join(map(str, compressed_coords)))
