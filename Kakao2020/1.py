def solution(s):
    if len(s) < 3:
        return len(s)

    answer = len(s)
    max_cand = int(len(s) / 2)
    for interval in range(1, max_cand + 1):
        start = interval
        res = []
        pre_s = s[0:interval]
        num = 1
        while True:
            now_s = s[start:start + interval]
            if now_s == pre_s:
                num += 1
            else:
                res.append([num, pre_s])
                num = 1
                pre_s = now_s

            if start > len(s):
                break
            start += interval
        len_cand = 0
        for k in range(len(res)):
            if res[k][0] == 1:
                len_cand += len(res[k][1])
            else:
                len_cand += len(str(res[k][0]))
                len_cand += len(res[k][1])
        answer = min(answer, len_cand)

    return answer
