from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        # Store all valid words in a set.
        # A set gives O(1) lookup and will also act as our "unvisited" set.
        wordSet = set(wordList)

        # If the destination doesn't exist,
        # transformation is impossible.
        if endWord not in wordSet:
            return 0

        # Queue stores:
        # (currentWord, currentTransformationLength)
        queue = deque([(beginWord, 1)])

        # Mark beginWord as visited.
        # (Only if it exists in the set.)
        wordSet.discard(beginWord)

        while queue:

            # Process the next word in BFS.
            word, steps = queue.popleft()

            # First time reaching endWord
            # is guaranteed to be the shortest path.
            if word == endWord:
                return steps

            # Try changing every character.
            for i in range(len(word)):

                # Replace current character with every letter.
                for ch in "abcdefghijklmnopqrstuvwxyz":

                    newWord = (
                        word[:i] +
                        ch +
                        word[i + 1:]
                    )

                    # If this is an unvisited valid word,
                    # visit it immediately.
                    if newWord in wordSet:

                        # Remove immediately so it is never
                        # inserted into the queue again.
                        wordSet.remove(newWord)

                        queue.append((newWord, steps + 1))

        # No transformation found.
        return 0

