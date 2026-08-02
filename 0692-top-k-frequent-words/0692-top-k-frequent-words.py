from collections import Counter

class Solution:
    def topKFrequent(self, words, k):
        freq = Counter(words)
        # Step 1: Sort alphabetically
        result = sorted(freq.items())
        # Step 2: Sort by frequency (highest first)
        result = sorted(result, key=lambda x: x[1], reverse=True)

        ans = []

        for i in range(k):
            ans.append(result[i][0])

        return ans