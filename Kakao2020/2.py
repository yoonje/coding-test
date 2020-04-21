def divide_uv(s):
    count_l = 0
    count_r = 0
    for i in range(len(s)):
        if s[i] == '(':
            count_l += 1
        else:  # s[i] == ')':
            count_r += 1
        if count_l == count_r:
            break
    return s[:i + 1], s[i + 1:]


def right(s):
    result = True
    count = 0
    for i in range(len(s)):
        if s[i] == '(':
            count += 1
        else:  # s[i] == ')':
            count -= 1
        if count < 0:
            result = False
            break
    return result


def solution(p):
    if p is '':  # 1번 조건
        return ''

    u, v = divide_uv(p)  # 2번 조건
    if right(u) == True:  # 3번 조건
        return u + solution(v)
    else:  # right(u) == False: 4번 조건
        answer = '('  # 4-1
        answer += solution(v)  # 4-2
        answer += ')'  # 4-3

        del_u = u[1:-1]  # 4-4
        for i in range(len(del_u)):
            if del_u[i] == '(':
                answer += ')'
            else:  # del_u[i] == ')':
                answer += '('
        return answer  # 4-5
