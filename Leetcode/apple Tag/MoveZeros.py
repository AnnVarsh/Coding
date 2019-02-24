class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
        nonzeropos = 0
        for i in range(len(nums)):
            num = nums[i]
            
            if (num != 0):
                nums[nonzeropos], nums[i] = nums[i], nums[nonzeropos]
                nonzeropos+=1