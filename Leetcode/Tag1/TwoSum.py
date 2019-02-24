class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        val_dict = {}
        
        for i in range(len(nums)):
            if target - nums[i] in val_dict:
                return [i,val_dict[target-nums[i]]]
            else:
                val_dict[nums[i]] = i