from collections import deque


def solution(cacheSize, cities):
    cities = [item.upper() for item in cities]
    cache_db = deque()
    answer = 0
    for item in cities:
        if item not in cache_db:
            if len(cache_db) < cacheSize:
                cache_db.append(item)
            elif cacheSize == 0 :
                pass
            else:
                cache_db.popleft()
                cache_db.append(item)
            answer += 5
        else:
            cache_db.remove(item)
            cache_db.append(item)
            answer += 1
    return answer


print(solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))
