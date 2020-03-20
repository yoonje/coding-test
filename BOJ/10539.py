sequence_num = int(input())
b_sequence = list(map(int, input().split()))
a_sequence = list()

for i, item in enumerate(b_sequence):
    i = i + 1
    data = item * i - sum(a_sequence[0:i])
    a_sequence.append(data)

for j in range(sequence_num):
    print(a_sequence[j], end=" ")
