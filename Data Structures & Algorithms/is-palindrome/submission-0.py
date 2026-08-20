from itertools import islice
class Solution:
    def isPalindrome(self, s: str) -> bool:
        str_input = list(c.lower() for c in s if c.isalnum())
        first_half = islice(str_input, len(str_input) // 2)
        second_half = reversed(str_input)
        return all(a == b for a, b in zip(first_half, second_half))