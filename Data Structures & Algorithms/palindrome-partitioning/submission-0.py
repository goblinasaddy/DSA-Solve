class Solution:
    def backtrack(self,start,s,path,result):
        if start == len(s):
            result.append(path.copy())
            return 

        for end in range(start,len(s)):
            part = s[start:end+1]

            if part==part[::-1]:
                path.append(part)

                self.backtrack(end+1,s,path,result)

                path.pop()

    def partition(self, s: str) -> List[List[str]]:
        result = []

        self.backtrack(0,s,[],result)
        return result
        