class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opening_brackets = {'{': '}', '(': ')', '[': ']'}
        closing_brackets = {'}': '{', ')': '(', ']': '['}
        for c in s:
            if c in opening_brackets:
                stack.append(c)
                continue
            if len(stack) == 0 or closing_brackets[c] != stack[-1]:
                return False
            stack.pop()
        return len(stack) == 0 
