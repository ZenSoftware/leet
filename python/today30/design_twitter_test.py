from design_twitter import Twitter

def test1():
    twitter = Twitter()
    twitter.postTweet(1, 5) # User 1 posts a new tweet (id = 5).
    assert twitter.getNewsFeed(1) == [5]  # User 1's news feed should return a list with 1 tweet id -> [5]. return [5]
    twitter.follow(1, 2)    # User 1 follows user 2.
    twitter.postTweet(2, 6) # User 2 posts a new tweet (id = 6).
    assert twitter.getNewsFeed(1) == [6,5]  # User 1's news feed should return a list with 2 tweet ids -> [6, 5]. Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.
    twitter.unfollow(1, 2)  # User 1 unfollows user 2.
    assert twitter.getNewsFeed(1) == [5]  # User 1's news feed should return a list with 1 tweet id -> [5], since user 1 is no longer following user 2.