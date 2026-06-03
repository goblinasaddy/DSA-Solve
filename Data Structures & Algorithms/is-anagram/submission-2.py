class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq_s = {}
        for st in s:
            if st not in freq_s:
                freq_s[st] = 1

            else:
                freq_s[st] += 1

        
        for st in t:
            if st not in freq_s:
                return False
            else:
                freq_s[st]-=1

        for i in freq_s.values():
            if i>0:
                return False

        return True

        

