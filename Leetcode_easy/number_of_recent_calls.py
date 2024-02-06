# Number of recent calls (https://leetcode.com/problems/number-of-recent-calls/description/?envType=study-plan-v2&envId=leetcode-75)

class RecentCounter:

    def __init__(self):
        self.q = deque()       

    def ping(self, t: int) -> int:

        self.q.append(t)
        if len(self.q)==1:
            return 1

        while t-self.q[0]>3000:
            self.q.popleft()

        return len(self.q)
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
