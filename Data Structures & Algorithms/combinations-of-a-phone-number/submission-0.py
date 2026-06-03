class Solution:
    def backtrack(self,index,path,digits,phone,result):

        if index==len(digits):
            result.append("".join(path))
            return

        letters = phone[digits[index]]

        for ch in letters:
            path.append(ch)
            self.backtrack(index+1,path,digits,phone,result)
            path.pop()
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        phone={
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz",
        }
        result = []
        self.backtrack(0,[],digits,phone,result)

        return result