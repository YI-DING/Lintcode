class Solution:
    """
    @param nums: an array of integers
    @return: the number of unique integers
    """
    def deduplication(self, nums):
        if not nums:
            return 0
        sett=set()
        count = 0
        pos = 0
        for i in range(len(nums)):
            if nums[i] not in sett:
                sett.add(nums[i])
                nums[i], nums[pos] = nums[pos], nums[i]
                pos += 1
                count += 1
        return count