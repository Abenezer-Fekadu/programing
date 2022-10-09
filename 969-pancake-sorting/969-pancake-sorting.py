class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:

        result = []
        for i in range(len(arr), 0, -1):
            index = self.get_max_index(arr, i)
               
#     Reverse Maximum
            arr[:index+1] = arr[:index+1][::-1]
#     Reverse up to index
            arr[:i] = arr[:i][::-1]
                        
            result.append(index+1)
            result.append(i)
            
        return result
    
    
    def get_max_index(self,nums, last):
        for i in range(last+1):
            if nums[i] == last:
                return i
            
    
    
            