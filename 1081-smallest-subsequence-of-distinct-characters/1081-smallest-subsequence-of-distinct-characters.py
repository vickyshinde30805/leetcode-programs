class Solution:
    def smallestSubsequence(self, s: str) -> str:
        count = {}
        for ch in s:
            count[ch] = count.get(ch, 0) + 1

        stack = []
        visited = set()

        for ch in s:
            count[ch] -= 1

            if ch in visited:
                continue

            while stack and ch < stack[-1] and count[stack[-1]] > 0:
                visited.remove(stack.pop())

            stack.append(ch)
            visited.add(ch)

        return "".join(stack)