class Solution:
    def foreignDictionary(self, words):
        graph = defaultdict(set)
        indegree = {}

        # Initialize all unique characters
        for word in words:
            for ch in word:
                indegree[ch] = 0

        # Build graph
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]

            # Invalid prefix case
            if len(w1) > len(w2) and w1.startswith(w2):
                return ""

            for c1, c2 in zip(w1, w2):
                if c1 != c2:
                    if c2 not in graph[c1]:
                        graph[c1].add(c2)
                        indegree[c2] += 1
                    break

        q = deque()

        for ch in indegree:
            if indegree[ch] == 0:
                q.append(ch)

        order = []

        while q:
            ch = q.popleft()
            order.append(ch)

            for nei in graph[ch]:
                indegree[nei] -= 1

                if indegree[nei] == 0:
                    q.append(nei)

        if len(order) != len(indegree):
            return ""

        return "".join(order)