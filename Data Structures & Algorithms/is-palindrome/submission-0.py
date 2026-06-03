class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.strip().lower()
        clean_text = re.sub(r"[^A-Za-z0-9]", "", s)
        i = 0
        j = len(clean_text)-1
        print(s)

        while i<j:
            if clean_text[i]!=clean_text[j]:
                return False
            else:
                i+=1
                j-=1
        return True



    
