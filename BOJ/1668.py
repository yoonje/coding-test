test_case = int(input())
data_list = list()
for _ in range(test_case):
    data_list.append(int(input()))

max = max(data_list)

left_count = 0
top = 0
for item in data_list:
    if item == max:
        left_count += 1
        break
    elif top >= item:
        continue
    else:
        top = item
        left_count += 1

data_list.reverse()

right_count = 0
top = 0
for item in data_list:
    if item == max:
        right_count += 1
        break
    elif top >= item:
        continue
    else:
        top = item
        right_count += 1

print(left_count)
print(right_count)

