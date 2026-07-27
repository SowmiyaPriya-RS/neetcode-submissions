class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i == '(' or i == '{' or i == '[':
                stack.append(i)
            else:
                if not stack:
                    return False
                top = stack[-1]
                if((i == ')' and top != '(') or 
                   (i == ']' and top != '[') or 
                   (i == '}' and top != '{')):
                    return False
                stack.pop()
        return not stack

        