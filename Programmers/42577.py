import re


def solution(phone_book):
    phone_book.sort(key=lambda x: len(x))
    for idx in range(len(phone_book)):
        for idx2 in range(idx + 1, len(phone_book)):
            if re.search("^"+phone_book[idx], phone_book[idx2]):
                return False
    return True


print(solution(["1195524421", "119", "97674223"]))  # false
print(solution(["123", "456", "789"]))  # true
