class Solution:
    def dfs(self,r,c,idx):
        if idx == len(self.word):
            return True

        if (
            r<0 or
            c<0 or
            r>=self.rows or
            c>=self.cols or
            self.board[r][c] != self.word[idx]):
            return False

        temp = self.board[r][c]
        self.board[r][c] = "#"

        found = (
            self.dfs(r+1,c,idx+1) or
            self.dfs(r-1,c,idx+1) or
            self.dfs(r,c+1,idx+1) or
            self.dfs(r,c-1,idx+1) 
        )
        self.board[r][c] = temp

        return found

    def exist(self, board: List[List[str]], word: str) -> bool:
        self.board = board
        self.word = word

        self.rows = len(board)
        self.cols = len(board[0])

        for r in range(self.rows):
            for c in range(self.cols):
                if self.dfs(r,c,0):
                    return True

        return False


















