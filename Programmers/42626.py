import heapq


def solution(scoville, K):
    answer = 0
    # 1. 힙 생성 및 초기화
    heapq.heapify(scoville)

    # 2. 스코빌 지수 섞기
    # 반복 조건 1. 힙이 비어있지 않아야 한다.
    # 반복 조건 2. 힙의 첫 원소(가장 작은 수)가 K 보다 작아야 한다.
    # 반복 조건 3. 힙에서 두 번째 원소를 꺼낼 수 있어야 합니다. 없다면, -1을 반환합니다.
    # 2-1. 힙의 첫 번째 요소 first 꺼냄
    # 2-2. 힙의 두 번째 요소 second 꺼냄
    # 2-3. 힘에 first + second * 2 를 저장함
    # 2-4. answer를 1 증가시킴.
    # 2-5. 조건들을 만족할 때까지 1-4 반복
    while scoville:
        first = heapq.heappop(scoville)
        if first >= K:
            break
        if len(scoville) <= 0:
            return -1
        second = heapq.heappop(scoville)
        heapq.heappush(scoville, first + second * 2)
        answer += 1
    return answer
