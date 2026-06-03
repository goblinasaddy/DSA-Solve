class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        max_count = 0
        best = 0
        l = 0

        for r,ch in enumerate(s):
            count[ch]+=1
            if count[ch]>max_count:
                max_count = count[ch]

            while (r-l+1) - max_count > k:
                count[s[l]]-=1
                l+=1

            win_len = r-l+1
            best = max(best,win_len)

        return best