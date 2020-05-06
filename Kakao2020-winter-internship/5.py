def check(num, stones, k):
    empty = 0
    for stone in stones:
        if stone >= num:
            empty = 0
        else:
            empty += 1
            if empty == k:
                return False
    else:
        return True


def solution(stones, k):
    min_n = min(stones)
    max_n = max(stones)
    answer = None
    while min_n <= max_n:
        mid = (min_n + max_n) // 2
        if check(mid, stones, k):
            answer = mid
            min_n = mid + 1
        else:
            max_n = mid - 1
    return answer


print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))  # 3
print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 1))  # 1
