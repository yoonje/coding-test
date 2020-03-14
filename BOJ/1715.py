import sys
import heapq

card_bundle_num = int(sys.stdin.readline())
heap = list()

for _ in range(card_bundle_num):
    heapq.heappush(heap, (int(sys.stdin.readline())))

compare_count = 0
while len(heap) != 1:
    data = heapq.heappop(heap)
    data2 = heapq.heappop(heap)
    compare_count += (data + data2)
    heapq.heappush(heap, data2 + data)

print(compare_count)
