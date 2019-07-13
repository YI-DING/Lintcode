class Solution:
    def search(self, A: List[int], target: int):
        if not A:
            return -1
        start, end = 0, len(A)-1
        #firstly find pivot position
        pivot = None
        if A[start] < A[end]:#unrotated
            pivot = 0
        else:
            while start+1 < end:
                mid = (start+end)//2
                if A[mid] > A[mid+1]:
                    pivot = mid+1
                    break
                else:
                    if A[mid] >= A[end]:
                        start = mid 
                    else:
                        end = mid 
            if pivot is None:
                pivot = end
        #pivot found. 
        if pivot == 0:
            start, end = 0, len(A)-1
        else:
            if A[pivot] <= target <= A[len(A)-1]:
                start, end = pivot, len(A)-1
            else:
                start, end = 0, pivot-1
        while start+1 < end:
            mid = (start+end)//2
            if A[mid] > target:
                end = mid
            else:
                start = mid
        if A[start] == target:
            return start
        elif A[end] == target:
            return end
        else:
            return -1