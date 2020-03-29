data = input()
count = 0
for i in range(1, len(data)):
    if data[i] != data[i - 1]:
        count += 1
print((count + 1) // 2)  # 바뀌는 구간+1 // 2
