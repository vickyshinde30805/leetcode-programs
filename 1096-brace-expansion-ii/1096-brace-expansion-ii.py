class Solution:
    def braceExpansionII(self, expression):

        def parse(i):
            res = set()
            cur = {""}

            while i < len(expression) and expression[i] != '}':
                
                if expression[i] == ',':
                    # Union: save current part
                    res |= cur
                    cur = {""}
                    i += 1

                elif expression[i] == '{':
                    # Parse inside braces
                    part, i = parse(i + 1)

                    # Concatenate
                    cur = {
                        a + b
                        for a in cur
                        for b in part
                    }

                else:
                    # Single character
                    cur = {
                        a + expression[i]
                        for a in cur
                    }
                    i += 1

            # Add the final part
            res |= cur

            # Skip '}'
            if i < len(expression) and expression[i] == '}':
                i += 1

            return res, i

        result, _ = parse(0)

        return sorted(result)