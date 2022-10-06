class TimeMap:
    def __init__(self):
        self.dic = defaultdict(list)
        
    def set(self, key, value, timestamp):
        self.dic[key].append([timestamp, value])

    def get(self, key, timestamp):
        arr = self.dic[key]
        l, r = 0, len(arr)
        
        while l < r:
            mid = (l + r) // 2
            if arr[mid][0] <= timestamp:
                l = mid + 1
            elif arr[mid][0] > timestamp:
                r = mid
        
        return "" if r == 0 else arr[r - 1][1]

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)