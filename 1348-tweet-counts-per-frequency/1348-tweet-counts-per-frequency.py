class TweetCounts:
    def __init__(self):
        self.tweet = defaultdict(list)
        self.time = { 'minute': 60, 'hour':60*60, 'day':60*60*24}

    def recordTweet(self, tweetName: str, time: int) -> None:
        self.tweet[tweetName].append(time)

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        n = ((endTime-startTime)//self.time[freq])+1
        ans = [0] * n
        for i in self.tweet[tweetName]:
            if startTime <= i <= endTime:
                ans[(i-startTime)//self.time[freq]]+=1
        return ans


# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)