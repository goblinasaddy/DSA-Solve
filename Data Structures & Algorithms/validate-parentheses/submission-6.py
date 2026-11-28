class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True

        mapping = {
            ")":"(",
            "]":"[",
            "}":"{"
        }
        stack = []
        for char in s:
            if char in mapping.values():
                stack.append(char)

            else:
                if not stack or stack.pop()!= mapping[char]:
                    return False
        if not stack:
            return True
        return False
