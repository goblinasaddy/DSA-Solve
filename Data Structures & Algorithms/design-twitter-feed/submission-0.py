from collections import defaultdict 
import heapq
class Twitter:

    def __init__(self):
        self.time = 0
        self.followMap = defaultdict(set)
        self.tweets = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time +=1

        self.tweets[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        
        self.followMap[userId].add(userId)

        heap = []

        for followee in self.followMap[userId]:

            if self.tweets[followee]:

                index = len(self.tweets[followee])-1
                time , tweetId = self.tweets[followee][index]

                heapq.heappush(
                    heap,
                    (-time, tweetId, followee, index-1)
                )

        result = []

        while heap and len(result)<10:

            negTime , tweetId, followee, index = heapq.heappop(heap)

            result.append(tweetId)

            if index >=0:
                time, tweetId = self.tweets[followee][index]

                heapq.heappush( 
                    heap,
                    (-time, tweetId, followee, index - 1) 
                )
        return result



    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
