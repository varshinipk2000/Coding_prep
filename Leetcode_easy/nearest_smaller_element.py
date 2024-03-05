# Nearest Smaller Element (https://www.interviewbit.com/problems/nearest-smaller-element/)

from collections import deque
class Solution:
	# @param A : list of integers
	# @return a list of integers
	def prevSmaller(self, A):
		
		stack = deque()
		res = [-1]*len(A)
		
		for i in range(0,len(A)):
			
			while stack and stack[-1]>=A[i]:
				stack.pop()
				
			if len(stack)==0:
				res[i] = -1
			else:
				res[i] = stack[-1]
				
			stack.append(A[i])
			
		return res
