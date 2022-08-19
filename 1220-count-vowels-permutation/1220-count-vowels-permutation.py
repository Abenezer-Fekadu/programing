class Solution:
    def countVowelPermutation(self, n: int) -> int:
        dp = {'a':1,'e':1,'i':1,'o':1,'u':1}
        mod=10**9+7    
        
        for i in range(n-1):
            check = {}
            for c in 'aeiou':
                if c == 'a':
                    check[c] = dp['e']
                elif c == 'e':
                    check[c] = dp['a'] + dp['i']
                elif c == "i":
                    check[c] = dp['a'] + dp['e'] + dp['o'] + dp['u']
                elif c == 'o':
                    check[c] = dp['i'] + dp['u']
                elif c == 'u':
                    check[c] = dp['a']
                    
            dp = check
        ans = sum(dp.values())
        return ans % mod