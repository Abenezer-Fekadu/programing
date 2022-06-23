class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key = lambda x : x[1])
        
        ans = []
        maxx = 0
        
        for i , j in courses:
            heappush(ans , -i)
            maxx = maxx + i
            if maxx > j:
                val = heappop(ans)
                maxx = maxx + val
        
        
        return len(ans)