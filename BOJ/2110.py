n, c = list(map(int, input().split(' ')))
array = []
for _ in range(n):
    array.append(int(input()))
array = sorted(array)
start = array[1] - array[0]
end = array[-1] - array[0]
result = 0
while (start <= end):
    mid = (start + end) // 2  # mid는 Gap을 의미합니다.
    value = array[0]
    count = 1
    for i in range(1, len(array)):
        if array[i] >= value + mid:
            value = array[i]
            count += 1
    if count >= c:  # C개 이상의 공유기를 설치할 수 있는 경우
        start = mid + 1
        result = mid
    else:  # C개 이상의 공유기를 설치할 수 없는 경우
        end = mid - 1
print(result)
