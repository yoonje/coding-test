def init(M):  # 배열 0으로 초기화 생성
    res = []
    for m in range(M):
        temp = []
        for n in range(M):
            temp.append(0)
        res.append(temp)
    return res


def padding(lock, N, M):  # sliding을 위한 0으로 padding
    T = N + 2 * (M - 1)
    res = []
    for m in range(T):
        temp = []
        for n in range(T):
            temp.append(0)
        res.append(temp)

    for i in range(N):
        for j in range(N):
            res[i + M - 1][j + M - 1] = lock[i][j]

    return res


def check(key, lock_padding):  # key와 padding 결과를 비교하여 check
    import copy
    T = len(lock_padding)
    M = len(key)
    for gap1 in range(T - M + 1):
        for gap2 in range(T - M + 1):
            res = True
            cand_padding = copy.deepcopy(lock_padding)
            for p in range(M):
                for q in range(M):
                    cand_padding[p + gap1][q + gap2] += key[p][q]
            check_area = []
            for p in range(M - 1, T - M + 1):
                temp = []
                for q in range(M - 1, T - M + 1):
                    temp.append(cand_padding[p][q])
                check_area.append(temp)

            for p in range(len(check_area)):
                for q in range(len(check_area)):
                    if check_area[p][q] != 1:
                        res = False
                        break
                if res == False:
                    break
            if res == True:
                return res
    return False


def solution(key, lock):
    M = len(key)
    N = len(lock)
    key = [key]

    # key 후보 다 뽑기
    for i in range(3):
        new_key = init(M)
        for p in range(M):
            for q in range(M):
                new_key[q][M - 1 - p] = key[-1][p][q]
        key.append(new_key)

    # lock padding
    lock_padding = padding(lock, N, M)

    answer = False
    for i in range(4):
        cand_key = key[i]
        if check(cand_key, lock_padding) == True:
            return True

    return answer
