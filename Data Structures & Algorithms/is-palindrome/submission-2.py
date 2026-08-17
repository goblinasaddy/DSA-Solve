class Solution:
    def isPalindrome(self, s: str) -> bool:

        clean_string = "".join(st for st in s if st.isalnum())
        clean_string = clean_string.lower()
        i = 0
        j = len(clean_string)-1

        while i<j:
            if clean_string[i]!=clean_string[j]:
                return False

            i+=1
            j-=1

        return True
            