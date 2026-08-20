from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        d1, d2 = defaultdict(int), defaultdict(int)
        for s_char, t_char in zip(s, t):
            d1[s_char] += 1
            d2[t_char] += 1
        return len(d1) == len(d2) and all(d1[c] == d2[c] for c in d1)