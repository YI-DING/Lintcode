'''Given an array of n objects with k different colors (numbered from 1 to k), 
sort them so that objects of the same color are adjacent, 
with the colors in the order 1, 2, ... k.'''
class Solution:
    """
    @param colors: A list of integer
    @param k: An integer
    @return: nothing
    """
    def sortColors2(self, colors, k):
        
        def quicksort(A, color, start):
        	end = len(A) - 1
        	while start <= end:
        		while start <= end and A[start] == color:
        			start += 1
        		while start <= end and A[end] != color:
        			end -= 1
        		if start <= end:
        			A[start], A[end] = A[end], A[start]
        			start += 1
        			end -= 1
        	return start 

        if not colors or k == 1:
        	return 
        #k >= 2:
        start = quicksort(colors, 1, 0)
        for i in range(k-2):
        	start = quicksort(colors, i+2, start)