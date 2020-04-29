def convert(value, n):
    T = "0123456789ABCDEF"
    q, r = divmod(value, n)
    if q == 0:
        return T[r]
    else:
        return convert(q, n) + T[r]


def solution(n, t, m, p):
    # 진법 n
    # 미리 구할 숫자의 갯수 t
    # 게임에 참가하는 인원 m
    # 튜브의 순서 p
    value = 0
    value_list = list()
    for i in range(t * m):
        value_list.append(convert(value, n))
        value += 1
    values = "".join(value_list)
    result = []
    print(value_list)
    print(values)
    for i in range(len(values)):
        if i % m == p - 1:
            result.append(values[i])
        if len(result) == t:
            break
    return "".join(result)
