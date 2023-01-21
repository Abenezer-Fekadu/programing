class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []
        def backtrack(i, address):            
            if i == len(s):
                if len(address) == 4:
                    ans.append( '.'.join(map(str,address)) )
                return
            
            
            if len(address) < 4:
                address.append(int(s[i]))          
                backtrack(i+1, address)         
                address.pop()       
                
        
            if address and (address[-1] != 0 and address[-1]*10 + int(s[i]) <= 255):
                lastItem = address[-1]
                address[-1] = lastItem*10+int(s[i])
                backtrack(i+1, address)                    
                address[-1] = lastItem 
                
        backtrack(0, [])
        return ans