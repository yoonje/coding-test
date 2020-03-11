import sys
n = int(sys.stdin.readline())
num_list = [0] * 10001
for _ in range(n):
    input_data = int(sys.stdin.readline())
    num_list[input_data] += 1

for idx in range(10001):
    for _ in range(num_list[idx]):
        print(idx)
