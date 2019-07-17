class Solution:
    """
    @param nums: an integer array
    @return: nothing
    """
    def moveZeroes(self, nums):
    	if not nums:
    		return 
    	head = 0
    	for number in nums:
    		if number != 0:
    			nums[head] = number
    			head += 1
    	for i in range(head,len(nums)):
    		if nums[i] != 0:
    			nums[i] = 0
    		

