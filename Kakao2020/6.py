from itertools import permutations


def check_available(weak, dist):
    i = 0
    for d in dist:
        bound = weak[i] + d
        while bound >= weak[i]:
            i += 1
            if i == len(weak):
                return True
    return False


def solution(n, weak, dist):
    if not weak:
        return 0

    for m in range(1, len(dist) + 1):
        for perm_dist in permutations(dist, m):
            new_weak = weak[:]
            for _ in range(len(weak)):
                if check_available(new_weak, perm_dist):
                    return m
                new_weak = new_weak[1:] + [n + new_weak[0]]
    return -1
