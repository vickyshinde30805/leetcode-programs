from itertools import permutations
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        wordsCount = Counter(words)
        n, wordLen = len(s), len(words[0])
        totalLen = wordLen * len(words)
        ans = []

        # we need to traverse s worldLen times
        for i in range(wordLen):
            curCount = defaultdict(int)

            # tarverse s with diff beginning index
            for j in range(i, n-wordLen+1, wordLen):

                # hashing a worldLen len string
                if s[j:j+wordLen] in wordsCount:
                    curCount[s[j:j+wordLen]] += 1

                # subtract a worldLen len string if the string in words
                if j >= totalLen and s[j-totalLen: j-totalLen+wordLen] in wordsCount:
                    curCount[s[j-totalLen: j-totalLen+wordLen]] -= 1

                if curCount == wordsCount:
                    ans.append(j-totalLen+wordLen)
        return ans
        
        return ans