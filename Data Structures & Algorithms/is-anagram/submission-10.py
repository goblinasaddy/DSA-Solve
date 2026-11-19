class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq = {}
        for char in s:
            if char not in freq:
                freq[char]=1
            else:
                freq[char]+=1


        for char in t:
            if char not in freq:
                return False
            else:
                freq[char]-=1

        for char,k in freq.items():
            if k >0:
                return False



        return True