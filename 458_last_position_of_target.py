def lastPosition(self, nums, target):
    # write your code here
    if not nums:
        return -1
    if len(nums) == 1:
        return 0 if nums[0] == target else -1
        
    start, end = 0, len(nums)-1
    while start+1 < end:
        mid = (start+end)//2
        if nums[mid] > target:
            end = mid-1
        else:
            start = mid
    if nums[end] == target:
        return end
    elif nums[start] == target:
        return start 
    else:
        return -1