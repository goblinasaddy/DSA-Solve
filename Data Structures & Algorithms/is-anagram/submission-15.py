class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq = Counter(s)

        for char in t:
            if char not in freq:
                return False

            else:
                freq[char]-=1

        for v in freq.values():
            if v>0: return False

        return True