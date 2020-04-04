import heapq


def solution(food_times, k):
    if sum(food_times) <= k:
        return -1
    heap = list()
    for idx, item in enumerate(food_times):
        heapq.heappush(heap, (item, idx + 1))
    sum_value = 0
    previous = 0
    length = len(food_times)
    while sum_value + ((heap[0][0] - previous) * length) <= k:
        now = heapq.heappop(heap)[0]
        sum_value += (now - previous) * length
        length -= 1
        previous = now
    # 남은 음식 중에서 몇 번째 음식인지 확인
    target = k - sum_value + 1
    length = len(heap)
    temp = (target - 1) // length
    result = sorted(heap, key=lambda x: x[1])
    target -= temp * length
    return result[target - 1][1]
