class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        # ---------------- Build Trie ----------------
        root = TrieNode()

        for word in words:
            node = root
            for ch in word:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            node.word = word

        rows = len(board)
        cols = len(board[0])

        result = []

        # ---------------- DFS ----------------
        def dfs(r, c, node):

            # Out of bounds
            if (
                r < 0 or
                c < 0 or
                r >= rows or
                c >= cols
            ):
                return

            ch = board[r][c]

            # Already visited or character not in Trie
            if ch == "#" or ch not in node.children:
                return

            node = node.children[ch]

            # Found a word
            if node.word:
                result.append(node.word)
                node.word = None      # avoid duplicates

            # Mark visited
            board[r][c] = "#"

            dfs(r + 1, c, node)
            dfs(r - 1, c, node)
            dfs(r, c + 1, node)
            dfs(r, c - 1, node)

            # Restore
            board[r][c] = ch

        # Start DFS from every cell
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root)

        return result