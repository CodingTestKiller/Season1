import sys
from sys import stdin

sys.setrecursionlimit(100000)

input = stdin.readline

s1 = input().strip()
s2 = input().strip()


def get_lcs(s1: str, s2: str, s1_index: int, s2_index: int, cache: dict) -> int:
    if s1_index < 1 or s2_index < 1:
        return 0
    try:
        return cache[s1_index, s2_index]
    except KeyError:
        pass

    if s1[s1_index-1] == s2[s2_index-1]:
        cache[s1_index, s2_index] = 1 + \
            get_lcs(s1, s2, s1_index-1, s2_index-1, cache)
    else:
        cache[s1_index, s2_index] = max(get_lcs(s1, s2, s1_index-1, s2_index, cache),
                                        get_lcs(s1, s2, s1_index, s2_index-1, cache))
    return cache[s1_index, s2_index]


cache = {}
print(get_lcs(s1, s2, len(s1), len(s2), cache))
