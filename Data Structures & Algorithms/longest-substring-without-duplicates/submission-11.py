class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if s==" " or n == 0: return 0

        i = 0
        j=1
        sett = set({0})
        # sett.add(s[0])
        res = 0
        while j<n:
            while s[j] in sett:
                sett.remove(s[i])
                i+=1

            sett.add(s[j])
            res = max(res,j-i+1)
            j+=1

        return res