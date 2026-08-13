class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {
            ")":"(",
            "]":"[",
            "}":"{"
        }
        for char in s:
            if char in mapping.values():
                stack.append(char)

            else:
                if not stack: return False

                if mapping[char]!=stack.pop(): return False

        return not stack 















