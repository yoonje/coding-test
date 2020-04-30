import re


def solution(files):
    return sorted(files, key=lambda x: (re.search('\D+', x.upper()).group(), int(re.search('[0-9]+', x).group())))
