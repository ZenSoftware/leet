# https://leetcode.com/problems/design-twitter/description/
from typing import List
from collections import defaultdict
from heapq import heapify, heappop, heappush

class Twitter:

    def __init__(self):
        self.tweets = defaultdict(list)
        self.followed = defaultdict(set)
        self.count = 0
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        index = len(self.tweets[userId]) - 1
        tweet = [self.count, tweetId, userId, index]
        self.tweets[userId].append(tweet)
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        # construct heap
        heap = []
        if self.tweets[userId]:
            heap.append(self.tweets[userId][-1])
        for followee in self.followed[userId]:
            if self.tweets[followee]:
                heap.append(self.tweets[followee][-1])
        heapify(heap)

        # construct result
        res = []
        while heap and len(res) < 10:
            count, tweetId, tweeterId, index = heappop(heap)
            res.append(tweetId)
            if index >= 0:
                tweet = self.tweets[tweeterId][index]
                heappush(heap, tweet)
        
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followed[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followed[followerId]:
            self.followed[followerId].remove(followeeId)