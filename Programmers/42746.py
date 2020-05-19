def solution(numbers):
    numbers = [str(x) for x in numbers]
    numbers.sort(key=lambda x: (x * 4)[:4], reverse=True)
    answer = "".join(numbers) if numbers[0] != "0" else "0"
    return answer
