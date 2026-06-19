class Solution:
    def isValid(self, s: str) -> bool:
        check = {
            '}':'{',
            ']':'[',
            ')':'('
        }
        stack = []
        for character in s:
            if character in check.values():
                stack.append(character)
            elif character in check.keys() and len(stack)>0:
                if check[character] == stack[-1]:
                    stack.pop()
                else:
                    stack.append(character)
            else:
                return False
        return len(stack) == 0