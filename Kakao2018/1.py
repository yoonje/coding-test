def solution(n, arr1, arr2):
    answer = []
    for item1, item2 in zip(arr1, arr2):
        ret_item = bin(item1 | item2)[2:]
        ret_item = '0' * (n - len(ret_item)) + ret_item
        ret_item = ret_item.replace('1', '#')
        ret_item = ret_item.replace('0', ' ')
        answer.append(ret_item)
    return answer


print(solution(6, [46, 33, 33, 22, 31, 50], [27, 56, 19, 14, 14, 10]))
