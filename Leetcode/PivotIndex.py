class Solution:
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        totalsum = sum(nums)
        subtotal = 0
        for i in range(len(nums)):
            left = subtotal
            right = totalsum - left - nums[i]
            if left == right:
                return i
            subtotal+=nums[i]
            
        return -1