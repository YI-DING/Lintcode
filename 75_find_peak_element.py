class Solution:
    def findPeakElement(self, A: List[int]):
        if not A:
            return None
        if len(A) == 1:
            return 0
        if len(A) == 2:
            return 0 if A[0] > A[1] else 1
        start, end = 0, len(A)-1
        while start+1 < end:
            mid = (start+end)//2
            if A[mid] > A[mid+1]:
                end = mid
            else:
                start = mid 
        return start if A[start] > A[end] else end