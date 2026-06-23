class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1,n2=len(s1),len(s2)
        if n1>n2:
            return False

        freq1=Counter(s1)
        freq2=Counter()

        for i in range(n2):
            freq2[s2[i]]+=1

            if i>=n1:
                left_char=s2[i-n1]
                freq2[left_char]-=1

                if freq2[left_char]==0:
                    del freq2[left_char]

            if freq2==freq1:
                return True
        return False