from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d1, d2 = defaultdict(int), defaultdict(int)
        for c in s:
            d1[c] += 1
        for c in t:
            d2[c] += 1
        return len(d1) == len(d2) and all(d1[c] == d2[c] for c in d1)