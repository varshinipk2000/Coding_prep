# LRU Cache (https://leetcode.com/problems/lru-cache/description/)

from collections import deque
class LRUCache:

    def __init__(self, capacity: int):
        self.stack = deque()
        self.cache = {}
        self.n = capacity        

    def get(self, key: int) -> int:
        if key in self.cache.keys():

            if key in self.stack:
                self.stack.remove(key)
            self.stack.append(key)

            return self.cache[key]
        return -1        

    def put(self, key: int, value: int) -> None:

        if self.n==len(self.cache) and key not in self.cache.keys():
            removekey = self.stack.popleft()
            del self.cache[removekey] #cache.del(remove)
        self.cache[key] = value
       
        if key in self.stack:
            self.stack.remove(key)
        self.stack.append(key)
