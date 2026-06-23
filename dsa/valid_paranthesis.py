class Solution(object):
    def isValid(self, s):
        stack = []
        pairs = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        for char in s:
            if char in "([{":
                stack.append(char)
            elif char in ")]}":
                if not stack:
                    return False
                top = stack.pop()
                if top != pairs[char]:
                    return False
        return len(stack) == 0