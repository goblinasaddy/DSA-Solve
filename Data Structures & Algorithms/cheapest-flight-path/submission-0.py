class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)

        for u,v,price in flights:
            graph[u].append((v,price))

        dist = [float('inf')]*n
        dist[src]=0
        q=deque([(src,0)])
        stops = 0
        while q and stops<=k:
            size = len(q)
            for _ in range(size):
                node,cost=q.popleft()
                for nei,price in graph[node]:
                    new_cost = cost+price
                    if new_cost<dist[nei]:
                        dist[nei]= new_cost
                        q.append((nei,new_cost))

            stops+=1

        return -1 if dist[dst]==float('inf') else dist[dst]