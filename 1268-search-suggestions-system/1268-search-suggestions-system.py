class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        ans = []
        for word in range(len(searchWord)):
            ans.append([])
            for prod in products:
                if prod.startswith(searchWord[:word+1]):
                    ans[word].append(prod)
                if len(ans[word]) == 3:
                    break
        return ans