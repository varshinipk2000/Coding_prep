# Valid Parenthesis (https://leetcode.com/problems/valid-parentheses/)

class Solution:
    def isValid(self, s: str) -> bool:

        if len(s)<=1:
            return False

        stack = deque()

        i=0
        while i<len(s):
            if s[i]=='(' or s[i]=='[' or s[i]=='{':
                stack.append(s[i])
            elif s[i]==')' and len(stack)>0 and stack[-1]=='(':
                stack.pop()
            elif s[i]==']' and len(stack)>0 and stack[-1]=='[':
                stack.pop()
            elif s[i]=='}' and len(stack)>0 and stack[-1]=='{':
                stack.pop()
            else:
                return False
            i+=1

        if len(stack)==0:
            return True
        return False        
