class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        n = len(words)
        words_set = set(words)

        # Top-Down
        memo = {}
        def dp(word):  
            if word not in memo:               
                max_length = 1
                for idx in range(len(word)):
                    new_word = word[:idx] + word[idx+1:]
                    if new_word in words_set:
                        max_length = max(max_length, 1 + dp(new_word))

                memo[word] = max_length
            return memo[word]
        
        return max(dp(word) for word in words)

        # Bottom-Up
        
        # dp = defaultdict(int)
        # for w in sorted(words, key=len):
        #     max_length = 1
        #     for i in range(len(w)):
        #         word = w[:i] + w[i+1:]
        #         if word in words_set:
        #             max_length = max(dp[word], 0) + 1

        #     dp[w] = max_length
        # return max(dp.values())

