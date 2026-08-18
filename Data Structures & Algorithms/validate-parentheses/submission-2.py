class Solution:
    def isValid(self, s: str) -> bool:
        a = []
        for i in range(len(s)):
            if s[i] in '*([{':
                a.append(s[i])
            else:
                if len(a) == 0:
                    return False
                if s[i] == ')' and a.pop() != '(':
                    return False
                elif s[i] == ']' and a.pop() != '[':
                    return False
                elif s[i] == '}' and a.pop() != '{':
                    return False
        if len(a) != 0:
            return False
        else:
            return True