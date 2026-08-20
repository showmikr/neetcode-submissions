from itertools import islice
class Solution:
    def isPalindrome(self, s: str) -> bool:
        first_half = (c.lower() for c in s if c.isalnum())
        second_half = (c.lower() for c in reversed(s) if c.isalnum())
        return all(a == b for a, b in zip(first_half, second_half))