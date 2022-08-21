class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        slen, tlen = len(stamp), len(target)
        ans = []
        
        covers = set()   
        for i in range(slen):
            for j in range(slen - i):
                covers.add('#' * i + stamp[i:slen-j] + '#' * j)
		
        check = '#' * tlen
		
        p = tlen - slen 
        while target != check:
            found = False
            for i in range(p, -1, -1):
                if target[i: i+slen] in covers:
                    target = target[:i] + '#' * slen + target[i+slen:] 
                    ans.append(i)
                    found = True
            if not found:   
                return []
        
        return ans[::-1]