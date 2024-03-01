# Repeat and missing number array (https://www.interviewbit.com/problems/repeat-and-missing-number-array/)

class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A):
        actualsum = len(A)*(len(A)+1)//2
        currsum = sum(A)
        hashmap = {}
        
        for ele in A:
            if ele in hashmap:
                a = ele
                break
            else:
                hashmap[ele] = 1
                
        b = actualsum - (currsum - ele)
        
        return [a,b]
