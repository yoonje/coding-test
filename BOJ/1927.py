import sys
import heapq

data_num = int(sys.stdin.readline())
heap = list()

for _ in range(data_num):
    data = int(sys.stdin.readline())
    if data == 0:
        if heap:
            print(heapq.heappop(heap))
        else:
            print("0")
    else:
        heapq.heappush(heap, data)
