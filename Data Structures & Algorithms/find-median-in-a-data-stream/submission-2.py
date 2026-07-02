import heapq

class MedianFinder:

    def __init__(self):

        # Max Heap (store negatives)
        self.small = []

        # Min Heap
        self.large = []

    def addNum(self, num):

        # Step 1:
        # Always push into max heap first.
        heapq.heappush(self.small, -num)

        # Step 2:
        # Ensure every element in left <= every element in right.
        if (
            self.small
            and self.large
            and
            -self.small[0] > self.large[0]
        ):
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        # Step 3:
        # Balance heap sizes.
        if len(self.small) > len(self.large) + 1:

            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        if len(self.large) > len(self.small) + 1:

            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)

    def findMedian(self):

        # Left heap bigger.
        if len(self.small) > len(self.large):
            return -self.small[0]

        # Right heap bigger.
        if len(self.large) > len(self.small):
            return self.large[0]

        # Same size.
        return (
            -self.small[0] + self.large[0]
        ) / 2