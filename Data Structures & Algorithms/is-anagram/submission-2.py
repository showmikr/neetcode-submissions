from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_map, t_map = Counter(s), Counter(t)
        return all(s_char in t_map and s_map[s_char] == t_map[s_char] for s_char in s_map)