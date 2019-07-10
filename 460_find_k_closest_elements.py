def kClosestNumbers(self, A, target, k):
    if not A or not target or k in (None,0):
        return []
    start, end = 0, len(A)-1
    #first the left and right num of target
    while start+1 < end:
        mid = (start+end)//2
        if A[mid] < target:
            start = mid
        else:
            end = mid
    if A[start] >= target:
        index = start
    elif A[end] >= target:
        index = end
    else:
        index = len(A)
    
    left, right = index-1, index
    result = []
    for _ in range(k):
        if left < 0:
            result.append(A[right])
            right += 1
        elif right > len(A)-1:
            result.append(A[left])
            left -=1
        elif abs(A[left]-target) > abs(A[right]-target):
            result.append(A[right])
            right +=1
        elif abs(A[left]-target) < abs(A[right]-target):
            result.append(A[left])
            left -= 1
        else:
            result.append(A[left])
            left -= 1
    return result