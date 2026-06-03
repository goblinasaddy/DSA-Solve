class Solution:
    def solve(self,row,board,result,n):
        if row==n:
            result.append(["".join(r) for r in board])
            return

        for col in range(n):
            if self.isSafe(board,row,col,n):
                board[row][col]="Q"
                self.solve(row+1,board,result,n)
                board[row][col]="."

    def isSafe(self,board,row,col,n):
        r=row
        c=col
        while r>=0:
            if board[r][c]=="Q":
                return False
            r-=1

        r=row
        c=col
        while r>=0 and c>=0:
            if board[r][c]=="Q":
                return False
            r-=1
            c-=1

        r=row
        c=col
        while r>=0 and c<n:
            if board[r][c]=="Q":
                return False
            r-=1
            c+=1

        return True
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["."]*n for _ in range(n)]
        result = []

        self.solve(0,board,result,n)

        return result        