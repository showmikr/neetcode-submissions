class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = dict()
        anchor = res = 0
        for i, c in enumerate(s):
            if c not in chars:
                chars[c] = i
                continue
            res = max(res, i - anchor)
            for j in range(anchor, chars[c]):
                del chars[s[j]]
            anchor = chars[c] + 1
            chars[c] = i
        return max(res, len(s) - anchor)