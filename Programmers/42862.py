def solution(n, lost, reserve):
    u = [1] * (n + 2)

    for i in reserve:
        u[i] += 1

    for i in lost:
        u[i] -= 1

    for i in range(1, n + 1):
        if u[i - 1] < 1 and u[i] > 1:
            u[i - 1:i + 1] = [1, 1]
        elif u[i] > 1 and u[i + 1] < 1:
            u[i:i + 2] = [1, 1]

    answer = n - len([e for e in u[1:] if e < 1])
    return answer
