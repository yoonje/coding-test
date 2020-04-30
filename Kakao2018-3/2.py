def solution(msg):
    compression_dict = dict()
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i, alpha in enumerate(alphabet):
        compression_dict[alpha] = i + 1

    answer = list()

    while msg:
        if msg in compression_dict.keys():
            answer.append(compression_dict[msg])
            break
        for i in range(1, len(msg)):
            if msg[:-i] in compression_dict.keys():
                answer.append(compression_dict[msg[:-i]])
                compression_dict.update({msg[:-i+1]: len(compression_dict) + 1})
                msg = msg[len(msg)-i:]
                break
    return answer


print(solution("KAKAO"))  # [11, 1, 27, 15]
print(solution("TOBEORNOTTOBEORTOBEORNOT"))  # [20, 15, 2, 5, 15, 18, 14, 15, 20, 27, 29, 31, 36, 30, 32, 34]
# print(solution("ABABABABABABABAB"))  # [1, 2, 27, 29, 28, 31, 30]
