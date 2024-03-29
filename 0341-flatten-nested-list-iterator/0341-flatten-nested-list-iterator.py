# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.list = []
        self.idx = -1
        def dfs(nestedList):
            if nestedList is None:
                return
            for i, num in enumerate(nestedList):
                if num.isInteger():
                    self.list.append(num.getInteger())
                else:
                    dfs(num.getList())
        dfs(nestedList)
       
    def next(self) -> int:
        num = self.list[0]
        self.list.pop(0)
        return num
       
    def hasNext(self) -> bool:
        return len(self.list) > 0
# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())