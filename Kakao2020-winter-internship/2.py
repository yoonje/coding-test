def solution(s):
    s = s[2:-2].split("},{")
    sorted_s = sorted(s, key=lambda x: len(x))
    answer = []
    check = set()
    for value in sorted_s:
        for each_value in value.split(","):
            if each_value not in check:
                answer.append(int(each_value))
                check.add(each_value)
                break
    return answer
