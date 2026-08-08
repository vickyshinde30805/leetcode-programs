from typing import List

class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        n, m = len(word1), len(word2)

        # Step 1: suffix match array
        suffix = [0] * (n + 1)
        j = m - 1
        for i in range(n - 1, -1, -1):
            if j >= 0 and word1[i] == word2[j]:
                j -= 1
            suffix[i] = m - 1 - j  # how many chars matched from end

        # Step 2: build answer greedily
        ans = []
        j = 0
        used = 0

        for i in range(n):
            if j == m:
                break

            # case 1: exact match
            if word1[i] == word2[j]:
                ans.append(i)
                j += 1

            # case 2: mismatch allowed
            elif used == 0:
                # check if we can still complete remaining using suffix
                remaining = m - (j + 1)
                if suffix[i + 1] >= remaining:
                    ans.append(i)
                    j += 1
                    used = 1

        return ans if j == m else []