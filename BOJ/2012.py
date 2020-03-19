N = int(input())

num_list = list()
sequence = list()
for i in range(1, N + 1):
    num_list.append(int(input()))
    sequence.append(i)

num_list.sort()

sum = 0
for idx, item in enumerate(num_list):
    sum += abs(sequence[idx] - item)

print(sum)