class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        clean_text = re.sub(r"[^A-Za-z0-9]", "", s)
        i = 0
        j = len(clean_text)-1


        while i<j:
            if clean_text[i]!=clean_text[j]:
                return False
            else:
                i+=1
                j-=1
        return True



    
