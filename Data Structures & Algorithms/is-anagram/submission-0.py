class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq= {}
        for st in s:
            if st not in freq:
                freq[st] = 1
            else:
                freq[st] += 1
        for i in t:
            if i not in freq:
                return False
            else:
                freq[i] -= 1
        for i in freq.values():
            if i == 1:
                return False
        return True
        