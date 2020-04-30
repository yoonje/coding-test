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