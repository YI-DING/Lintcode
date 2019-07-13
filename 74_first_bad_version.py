def findFirstBadVersion(self, n):
    if not n:
        return None
    if n == 1:
        return 1
    start, end = 1, n
    while start+1 < end:
        mid = (start+end)//2
        if SVNRepo.isBadVersion(mid):#mid is bad
            end = mid 
        else:#mid is good
            start = mid+1
    return start if SVNRepo.isBadVersion(start) else end