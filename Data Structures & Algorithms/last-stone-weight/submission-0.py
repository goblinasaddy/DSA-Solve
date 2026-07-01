
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        while len(stones)>1:

            stones.sort()
            if stones[-1] != stones[-2]:
                stone = stones[-1] - stones[-2]
                stones.pop()
                stones.pop()
                stones.append(stone)
            else:
                stones.pop()
                stones.pop()

        return stones[0]


        