import re

target_str = input()
str = input()

p = re.compile(str)  # 소문자(a-z)가 1회 이상 반복되는 걸 찾아와라.
m = p.findall(target_str)
print(len(m))
