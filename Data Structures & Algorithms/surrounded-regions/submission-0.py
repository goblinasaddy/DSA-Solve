
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Modify board in-place.
        """

        if not board:
            return

        ROWS = len(board)
        COLS = len(board[0])

        # DFS to mark all border-connected 'O' as safe ('S')
        def dfs(r, c):

            # Out of bounds or not an 'O'
            if (
                r < 0 or
                c < 0 or
                r >= ROWS or
                c >= COLS or
                board[r][c] != "O"
            ):
                return

            # Mark current cell as Safe
            board[r][c] = "S"

            # Explore 4 directions
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        # -------------------------------
        # Step 1:
        # DFS from all BORDER 'O's
        # -------------------------------

        # Left and Right borders
        for r in range(ROWS):

            if board[r][0] == "O":
                dfs(r, 0)

            if board[r][COLS - 1] == "O":
                dfs(r, COLS - 1)

        # Top and Bottom borders
        for c in range(COLS):

            if board[0][c] == "O":
                dfs(0, c)

            if board[ROWS - 1][c] == "O":
                dfs(ROWS - 1, c)

        # -------------------------------
        # Step 2:
        # Flip surrounded regions
        # -------------------------------
        for r in range(ROWS):
            for c in range(COLS):

                # Surrounded region
                if board[r][c] == "O":
                    board[r][c] = "X"

                # Safe region
                elif board[r][c] == "S":
                    board[r][c] = "O"

