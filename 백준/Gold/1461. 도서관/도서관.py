def solve():
    N, M = map(int, input().split())  # N: 책의 개수, M: 한 번에 옮길 수 있는 책의 개수
    books = list(map(int, input().split()))

    # 음수와 양수로 분리
    positive = []
    negative = []
    for book in books:
        if book > 0:
            positive.append(book)
        else:
            negative.append(book)

    # 절대값이 큰 순서대로 정렬
    positive.sort(reverse=True)
    negative.sort()

    # 각 그룹에서 가장 멀리 떨어진 책을 가져다 놓기
    def calculate_distance(locations):
        distance = 0
        for i in range(0, len(locations), M):
            distance += abs(locations[i]) * 2  # 왕복 거리
        return distance

    total_distance = calculate_distance(positive) + calculate_distance(negative)

    # 마지막으로 가장 먼 책을 가져다 놓고 돌아오지 않음
    if positive and negative:
        total_distance -= max(abs(positive[0]), abs(negative[0]))
    elif positive:
        total_distance -= abs(positive[0])
    elif negative:
        total_distance -= abs(negative[0])

    print(total_distance)

# 실행
solve()
