class Solution:
    def isValid(self, s: str) -> bool:
        endMap = {']':'[',')':'(','}':'{'}
        stack = []
        for sym in s:
            if sym in endMap:
                if stack and stack[-1] == endMap[sym]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(sym)
        return True if len(stack) == 0 else False