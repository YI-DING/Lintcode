class Solution:
    """
    @param nums: an array of integers
    @param s: An integer
    @return: an integer representing the minimum size of subarray
    """
    def minimumSize(self, nums, s):
        fast, slow, maxx, summ = -1, 0, float("inf"), 0 
        while fast <= len(nums) - 1:
            if summ < s:
                fast += 1
                if fast <= len(nums) - 1:
                    summ += nums[fast]
            elif summ == s:
                maxx = min(maxx, fast - slow + 1)
                fast += 1
                if fast <= len(nums) - 1:
                    summ += nums[fast]
                summ -= nums[slow]
                slow += 1
            else:
                maxx = min(maxx, fast - slow + 1)
                summ -= nums[slow]
                slow += 1
        return maxx if maxx != float("inf") else -1