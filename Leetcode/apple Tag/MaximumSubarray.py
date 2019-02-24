class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        cursum = maxsofar = nums[0]
        
        for i in nums[1:]:
            cursum = max(i, cursum + i)
            maxsofar = max(maxsofar, cursum)
            
        return maxsofar