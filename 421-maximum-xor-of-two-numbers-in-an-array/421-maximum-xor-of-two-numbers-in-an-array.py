class Trie():
    def __init__(self):
        self.children = {}
        self.num = 0
        
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        root = Trie()
        
        def search(num):
            node = root
            for i in range(31, -1, -1):
                val = 1 if num & (1 << i) else 0
                if 1-val in node.children:
                    node = node.children[1-val] 
                else: 
                    node = node.children[val] 
            
            return node.num
                
        for num in nums:
            node = root
            for i in range(31, -1, -1):
                val = 1 if num & (1 << i) else 0
                if val not in node.children:
                    node.children[val] = Trie()
                node = node.children[val]
            node.num = num
                    
        ans = 0
        for num in nums:
            mul = search(num)
            ans = max(ans, num ^ mul)        
        
        return ans
    