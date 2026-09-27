class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []

        for ch in s:
            if ch == ')':
                # Take characters until '('
                temp = []

                while stack[-1] != '(':
                    temp.append(stack.pop())

                # Remove '('
                stack.pop()

                # Add reversed substring back
                stack.extend(temp)

            else:
                stack.append(ch)

        return ''.join(stack)