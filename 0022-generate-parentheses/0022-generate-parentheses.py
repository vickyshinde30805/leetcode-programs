class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        result = []

        def backtrack(current, open_count, close_count):
            # If the string has 2*n parentheses, it is complete
            if len(current) == 2 * n:
                result.append(current)
                return

            # We can add '(' if we still have some left
            if open_count < n:
                backtrack(current + "(", open_count + 1, close_count)

            # We can add ')' only if it won't make the string invalid
            if close_count < open_count:
                backtrack(current + ")", open_count, close_count + 1)

        backtrack("", 0, 0)
        return result