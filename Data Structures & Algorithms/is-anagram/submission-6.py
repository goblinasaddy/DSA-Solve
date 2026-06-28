class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq={}
        
        for i in range(len(s)):
            if s[i] not in freq:
                freq[s[i]]=1
            else:
                freq[s[i]]+=1

        for i in range(len(t)):
            if t[i] not in freq:
                return False

            else:
                freq[t[i]]-=1


        for i in freq.values():
            if i != 0:
                return False

        return True