def solution(arr):
    sorted_arr = sorted(arr)
    for i in range(1, len(arr) + 1):
        if i == sorted_arr[i-1]:
            continue
        return False
    return True
