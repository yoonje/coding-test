import heapq
import copy

K, N = map(int, input().split())
p_list = list(map(int, input().split()))

lst, ck = copy.deepcopy(p_list), set()

heapq.heapify(lst)
ith = 0

while ith < N:
    mn = heapq.heappop(lst)
    if mn in ck:
        continue
    ith += 1
    ck.add(mn)
    for i in p_list:
        heapq.heappush(lst, mn * i)

print(mn)
