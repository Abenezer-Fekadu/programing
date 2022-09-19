class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        contents = defaultdict(list)
        
        for i in range(len(paths)):            
            path = paths[i].split()
            for i in range(1, len(path)):
                lst = path[i].split("(")
                
                contents[lst[1][:-1]].append(path[0] + '/' + lst[0])
        
        ans = []
        for val in contents.values():
            if len(val) > 1:
                ans.append(val)
                
        return ans