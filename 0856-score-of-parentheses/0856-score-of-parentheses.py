class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]

        for i in range(len(s)):
            if s[i] == '(':
                stack.append(0)
            else:
                x = stack.pop()

                if x == 0:
                    score = 1
                else:
                    score = 2 * x

                stack[-1] += score

        return stack[0]