# Min Stack (https://leetcode.com/problems/min-stack/description/)

from collections import deque
class MinStack:

    def __init__(self):
        self.minval = 100000000000
        self.stack = deque()
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.minval = min(self.minval, val)   
        

    def pop(self) -> None:
        ele = self.stack.pop()
        if ele==self.minval and self.minval not in self.stack and self.stack:
            self.minval = min(self.stack)    
        if len(self.stack)==0:
            self.minval = 10000000000

    def top(self) -> int:
        return self.stack[-1]        

    def getMin(self) -> int:
        return self.minval
