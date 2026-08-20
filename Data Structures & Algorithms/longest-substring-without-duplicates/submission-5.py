class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left_ptr, res = 0, 0
        char_set = set()
        for right_ptr, right_char in enumerate(s):
            while right_char in char_set:
                char_set.remove(s[left_ptr])
                left_ptr += 1
            char_set.add(right_char)
            res = max(right_ptr - left_ptr + 1, res)
        return res