class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        freq_1,freq_2 = {},{}

        for i in range(len(s)):
            freq_1[s[i]] = freq_1.get(s[i],0)+1
            freq_2[t[i]] = freq_2.get(t[i],0)+1

        return freq_1 == freq_2