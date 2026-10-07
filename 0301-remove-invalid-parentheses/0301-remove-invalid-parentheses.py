class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        def is_valid(string):
            count = 0

            for ch in string:
                if ch == '(':
                    count += 1
                elif ch == ')':
                    count -= 1

                    if count < 0:
                        return False

            return count == 0

        queue = [s]
        visited = {s}

        while queue:
            valid_strings = []

            for string in queue:
                if is_valid(string):
                    valid_strings.append(string)

            if valid_strings:
                return valid_strings

            next_queue = []

            for string in queue:
                for i in range(len(string)):
                    if string[i] not in "()":
                        continue

                    new_string = string[:i] + string[i + 1:]

                    if new_string not in visited:
                        visited.add(new_string)
                        next_queue.append(new_string)

            queue = next_queue

        return [""]