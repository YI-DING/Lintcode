def partitionArray(self, nums, k):
    left, right = 0, len(nums) - 1
    while left <= right:
        while left <= right and nums[left] < k:
            left += 1
        while left <= right and nums[right] >= k:
            right -= 1
        if left <= right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
    return left