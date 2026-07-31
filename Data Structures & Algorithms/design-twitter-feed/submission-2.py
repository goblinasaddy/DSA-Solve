
from collections import defaultdict
import heapq


class Twitter:

    def __init__(self):
        # Global timestamp (increases with every tweet)
        self.time = 0

        # user -> set of users they follow
        self.followMap = defaultdict(set)

        # user -> list of (timestamp, tweetId)
        # Tweets are naturally stored in chronological order.
        self.tweets = defaultdict(list)


    def postTweet(self, userId: int, tweetId: int) -> None:
        # Assign a new timestamp
        self.time += 1

        # Save the tweet
        self.tweets[userId].append((self.time, tweetId))


    def getNewsFeed(self, userId: int):

        # User should always see their own tweets.
        self.followMap[userId].add(userId)

        # Max Heap
        # (-time, tweetId, followee, previousTweetIndex)
        heap = []

        # Put the newest tweet of every followed user into the heap.
        for followee in self.followMap[userId]:

            if self.tweets[followee]:

                # Index of latest tweet
                index = len(self.tweets[followee]) - 1

                time, tweetId = self.tweets[followee][index]

                heapq.heappush(
                    heap,
                    (-time, tweetId, followee, index - 1)
                )

        result = []

        # Extract the 10 most recent tweets.
        while heap and len(result) < 10:

            negTime, tweetId, followee, index = heapq.heappop(heap)

            # Add current newest tweet
            result.append(tweetId)

            # Push the previous tweet of the same user.
            if index >= 0:

                time, tweetId = self.tweets[followee][index]

                heapq.heappush(
                    heap,
                    (-time, tweetId, followee, index - 1)
                )

        return result


    def follow(self, followerId: int, followeeId: int):
        # Follow a user
        self.followMap[followerId].add(followeeId)


    def unfollow(self, followerId: int, followeeId: int):
        # Prevent errors if not already following
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)

