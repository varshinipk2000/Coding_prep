# Online Stock Span (https://leetcode.com/problems/online-stock-span/)

from collections import deque
class StockSpanner:

    def __init__(self):
        self.stack = deque()        

    def next(self, price: int) -> int:
        """n = len(self.stack)
        while self.stack and price>=self.stack[n-1]:
            n-=1
            if n-1<0:
                break
        c = len(self.stack)-n+1
        self.stack.append(price)
        return c  """    
        c = 1
        while self.stack and self.stack[-1][0]<=price:
            ele = self.stack.pop()
            c+=ele[1]
        self.stack.append((price,c))
        return c
