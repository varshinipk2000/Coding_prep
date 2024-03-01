# Merge Intervals (https://leetcode.com/problems/merge-intervals/description/)

class Solution:
    def merge(self, interval: List[List[int]]) -> List[List[int]]:

        if len(interval)==1:
            return interval

        interval.sort()

        start = interval[0][0]
        end = interval[0][1]
        res = []

        for i in interval[1:]:
            if start<i[0] and end<i[0]:
                res.append([start,end])
                start = i[0]
                end = i[1]
            else:
                if start>i[0]:
                    start = i[0]
                if end>=i[0] and end<i[1]:
                    end = i[1]
                    
        res.append([start,end])
        return res      
